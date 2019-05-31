from shexer.io.sparql.query import query_endpoint_po_of_an_s, query_endpoint_single_variable

_DEF_PRED_VARIABLE = "?p"
_DEF_PRED_ID = "p"

_DEF_OBJ_VARIABLE = "?o"
_DEF_OBJ_ID = "o"


class SGraph(object):

    def __init__(self):
        pass

    def yield_p_o_triples_of_target_nodes(self, target_nodes, depth, classes_at_last_level=True, instantiation_property=None, already_visited=None):
        raise NotImplementedError()

    def query_single_variable(self, str_query, variable_id):
        raise NotImplementedError()


class EndpointSGraph(SGraph):

    def __init__(self, endpoint_url):
        super().__init__()
        self._endpoint_url = endpoint_url

    def query_single_variable(self, str_query, variable_id):
        return query_endpoint_single_variable(variable_id=variable_id,
                                              str_query=str_query,
                                              endpoint_url=self._endpoint_url)

    def yield_p_o_triples_of_target_nodes(self, target_nodes, depth, classes_at_last_level=True, instantiation_property=None, already_visited=None):
        """
        If it is provided, the param already_visited can be modified during the execution of this method.
        The set already_visited can be used to avoid repetition of triples calling this methodd repeatedly
        for different node selectors in a shape map.

        :param target_nodes:
        :param depth:
        :param classes_at_last_level:
        :param instantiation_property:
        :param already_visited:
        :return:
        """
        current_already_visited = set() if already_visited is None else already_visited
        list_of_current_target_nodes = target_nodes
        new_target_nodes = []
        while depth > 0:
            for a_node in list_of_current_target_nodes:
                if a_node not in already_visited:
                    current_already_visited.add(a_node)
                    for a_triple in self.yield_get_p_o_triples_of_an_s(a_node):
                        yield a_triple
                        if self._is_an_unprefixed_iri(a_triple[2]):
                            new_target_nodes.append(a_triple[2])
            depth -= 1
            list_of_current_target_nodes = new_target_nodes
            new_target_nodes = []
            if depth == 0 and classes_at_last_level:
                for a_node in list_of_current_target_nodes:
                    if a_node not in current_already_visited:
                        for a_triple in self.yield_class_triples_of_an_s(target_node=a_node,
                                                                         instantiation_property=instantiation_property):
                            yield a_triple



    def _is_an_unprefixed_iri(self, an_iri):
        if an_iri[0] == "<" and an_iri[-1] == ">":
            return True
        return False


    def yield_class_triples_of_an_s(self, target_node, instantiation_property):
        """
        Here it expects unprefixed URIs. So there is no stage of namespaces management to build a query.

        :param target_node:
        :param instantiation_property:
        :return:
        """
        str_query = "SELECT {0} WHERE {{ <{1}> <{2}> {0} . }}".format(_DEF_OBJ_VARIABLE, target_node, instantiation_property)
        for an_elem in query_endpoint_single_variable(endpoint_url=self._endpoint_url,
                                                      str_query=str_query,
                                                      variable_id=_DEF_OBJ_ID):
            yield (target_node, instantiation_property, an_elem)


    def yield_get_p_o_triples_of_an_s(self, target_node):
        """
        Here it expects unprefixed URIs. So there is no stage of namespaces management to build a query.

        :param target_node:
        :return:
        """
        str_query = "SELECT {0} {1} WHERE {{ <{2}> {0} {1} .}} ".format(_DEF_PRED_VARIABLE, _DEF_OBJ_VARIABLE, target_node)
        for a_tuple_po in query_endpoint_po_of_an_s(endpoint_url=self._endpoint_url,
                                                    str_query=str_query,
                                                    p_id=_DEF_PRED_ID,
                                                    o_id=_DEF_OBJ_ID):
            yield target_node, a_tuple_po[0], a_tuple_po[1]
