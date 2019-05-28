
class NodeSelector(object):

    def __init__(self, raw_selector):
        self._raw_selector = raw_selector

    def get_target_nodes(self, endpoint_base_uri=None):
        """
        It return a list of target URIs. It may require to execute some query against a given endpoint

        :return:
        """
        raise NotImplementedError()




class NodeSelectorNoSparql(NodeSelector):

    def __init__(self, raw_selector, taregt_node):
        super().__init__(raw_selector)
        self._target_nodes = [taregt_node]

    def get_target_nodes(self, endpoint_base_uri=None):
        return self._target_nodes


class NodeSelectorSparql(NodeSelector):

    def __init__(self, raw_selector, sparql_query_selector):
        super().__init__(raw_selector)
        self._sparql_query_selector = sparql_query_selector

