
class NodeSelector(object):

    def __init__(self, raw_selector):
        self._raw_selector = raw_selector

    def get_target_nodes(self, endpoint_base_uri=None):
        """
        It return a list of target URIs. It may require to execute some query against a given endpoint

        :return:
        """
        raise NotImplementedError()

    @property
    def raw_selector(self):
        return self._raw_selector


########################################################


class NodeSelectorNoSparql(NodeSelector):

    def __init__(self, raw_selector, taregt_node):
        super().__init__(raw_selector)
        self._target_nodes = [taregt_node]

    def get_target_nodes(self, endpoint_base_uri=None):
        return self._target_nodes


########################################################

from shexer.io.sparql.query import query_endpoint_single_variable


class NodeSelectorSparql(NodeSelector):

    def __init__(self, raw_selector, sparql_query_selector, id_variable_query):
        super().__init__(raw_selector)
        self._sparql_query_selector = sparql_query_selector
        self._id_variable_query = id_variable_query

    @property
    def sparql_query_selector(self):
        return self._sparql_query_selector

    def get_target_nodes(self, endpoint_base_uri=None):
        return query_endpoint_single_variable(variable_id=self._id_variable_query,
                                              str_query=self._sparql_query_selector,
                                              endpoint_url=endpoint_base_uri)


