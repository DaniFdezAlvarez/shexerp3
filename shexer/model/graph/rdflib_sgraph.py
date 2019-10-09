from rdflib import URIRef
from shexer.model.graph.abstract_sgraph import SGraph

class RdflibSgraph(SGraph):

    def __init__(self, rdflib_graph):
        super().__init__()
        self._rdflib_graph = rdflib_graph

    def query_single_variable(self, str_query, variable_id):
        rows_res = self._rdflib_graph.query(str_query)
        return [str(a_row[0]) for a_row in rows_res]


    def yield_p_o_triples_of_an_s(self, target_node):
        for s, p ,o in self._rdflib_graph.triples((URIRef(target_node), None, None)):
            yield str(s), str(p), str(o)


    def yield_class_triples_of_an_s(self, target_node, instantiation_property):
        for s ,p, o in self._rdflib_graph.triples((URIRef(target_node), URIRef(instantiation_property), None)):
            yield str(s), str(p), str(o)