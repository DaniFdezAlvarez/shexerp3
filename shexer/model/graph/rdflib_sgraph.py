from rdflib import URIRef, Graph
from shexer.model.graph.abstract_sgraph import SGraph

class RdflibSgraph(SGraph):

    def __init__(self, rdflib_graph=None, source_file=None, format="turtle"):
        """
        Pass an rdflib.Graph object or the params source_file and format to parse a local rdf

        :param rdflib_graph:
        :param source_file:
        :param format:
        """
        super().__init__()
        self._rdflib_graph = rdflib_graph if rdflib_graph is not None else self._build_rdflib_graph(source=source_file,
                                                                                                    format=format)

    def query_single_variable(self, str_query, variable_id):
        rows_res = self._rdflib_graph.query(str_query)
        return [str(a_row[0]) for a_row in rows_res]


    def yield_p_o_triples_of_an_s(self, target_node):
        for s, p ,o in self._rdflib_graph.triples((URIRef(target_node), None, None)):
            yield str(s), str(p), str(o)


    def yield_class_triples_of_an_s(self, target_node, instantiation_property):
        for s ,p, o in self._rdflib_graph.triples((URIRef(target_node), URIRef(instantiation_property), None)):
            yield str(s), str(p), str(o)


    def _build_rdflib_graph(self, source, format):
        result = Graph()
        result.parse(source=source, format=format)
        return result