from shexer.utils.dict import reverse_keys_and_values
from shexer.utils.uri import remove_corners
from shexer.model.node_selector import NodeSelectorNoSparql, NodeSelectorSparql
from rdflib.plugins import sparql
import re

_QUOTES = ["'", '"']
_WHITES_REGEX = re.compile(" +")

_FOCUS_LOWER = "focus"
_WILDCARD = "_"

_FOCUS_VARIABLE = "?f"
_WILDCARD_VARIABLE = "?x"


class NodeSelectorParser(object):

    def __init__(self, namespaces_prefix_dict):
        self._prefix_namespace_dict = reverse_keys_and_values(namespaces_prefix_dict)

    def parse_node_selector(self, raw_selector):
        raw_selector = raw_selector.strip()
        if raw_selector.startswith("<"):
            return self._parse_unprefixed_node_selector(raw_selector)
        elif raw_selector.startswith("{"):
            return self._parse_focus_expression(raw_selector)
        elif raw_selector.startswith("SPARQL"):
            return self._parse_sparql_expression(raw_selector)
        else:
            return self._parse_prefixed_node_selector(raw_selector)

    def _parse_unprefixed_node_selector(self, raw_selector):
        return NodeSelectorNoSparql(raw_selector=raw_selector,
                                    taregt_node=remove_corners(raw_selector))

    def _parse_prefixed_node_selector(self, raw_selector):
        for a_prefix in self._prefix_namespace_dict:
            if raw_selector.startswith(a_prefix + ":"):
                return NodeSelectorNoSparql(raw_selector=raw_selector,
                                            taregt_node=self._unprefix_uri(prefix=a_prefix,
                                                                           uri=raw_selector))

    def _parse_focus_expression(self, raw_selector):
        if raw_selector[0] != "{" or raw_selector[-1] != "}":
            raise ValueError("The following node selector is not surrounded by {}: " * raw_selector)
        raw_string = raw_selector[1:-1].strip()
        raw_string = _WHITES_REGEX.sub(" ", raw_string)
        pieces = raw_string.split(" ")
        if len(pieces) != 3:
            self._focus_node_error(raw_selector)
        subject_for_query, focus_count = self._parse_subj_obj_focus_expression(pieces[0], 0)
        predicate_for_query = self._parse_uri_focus_expression(pieces[0])
        object_for_query, focus_count = self._parse_subj_obj_focus_expression(pieces[2], focus_count)

        if focus_count != 1:
            raise ValueError("The node selector must have exactly one FOCUS")

        query = self._turn_focus_exp_tokens_into_query(subject_for_query, predicate_for_query, object_for_query)
        return NodeSelectorSparql(raw_selector=raw_selector,
                                  sparql_query_selector=query)

    def _turn_focus_exp_tokens_into_query(self, subj, pred, obj):
        string_query = "SELECT " + _FOCUS_VARIABLE + "WHERE {" + subj + " " + pred + " " + obj + " . }"
        return sparql.prepareQuery(string_query)

    def _parse_subj_obj_focus_expression(self, token, focus_count):
        if token.lower() == _FOCUS_LOWER:
            return _FOCUS_VARIABLE, focus_count + 1
        elif token == _WILDCARD:
            return _WILDCARD_VARIABLE, focus_count
        else:
            return self._parse_uri_focus_expression(token), focus_count

    def _parse_uri_focus_expression(self, token):
        if token.endswith(">"):
            if token.startswith("<"):
                return token
        else:
            for a_prefix in self._prefix_namespace_dict:
                if token.startswith(a_prefix + ":"):
                    return self._unprefix_uri(prefix=a_prefix,
                                              uri=token)
        raise ValueError("URI not well formed or with an unknown prefix: " + token)

    def _unprefix_uri(self, prefix, uri):
        return uri.replace(prefix + ":", self._prefix_namespace_dict[prefix])

    def _parse_sparql_expression(self, raw_selector):
        raw_string = raw_selector.replace("SPARQL", "")
        raw_string = raw_string.strip()
        if raw_string[0] in _QUOTES and raw_string[-1] in _QUOTES:
            try:
                return self._parse_single_variable_select_query(raw_string[1:-1])
            except BaseException as e:
                e.message = "The SPARQL query of the next node selector is not well formed: " \
                            + raw_selector + ". Cause: " + e.message
        raise ValueError("The SPARQL query of the next node selector is not surrounded by quotes: " + raw_selector)

    @staticmethod
    def _focus_node_error(raw_selector):
        raise ValueError("This focus node expression cant be parsed: " + raw_selector)

    @staticmethod
    def _parse_single_variable_select_query(string_query):
        # Is the query well-formed?
        candidate_query = sparql.prepareQuery(string_query)
        # Is it a select query?
        if "select" not in string_query[:string_query.find("{")]:
            raise ValueError("The SPARQL query is not a SELECT query")
        # Does it have a single variable
        if string_query[:string_query.find("{")].count("?") != 1:
            raise ValueError("The SPARQL query must have a single variable")

        return NodeSelectorSparql(raw_selector=string_query,
                                  sparql_query_selector=candidate_query)
