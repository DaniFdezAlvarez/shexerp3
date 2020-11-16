from shexer.io.graph.yielder.rdflib_triple_yielder import RdflibParserTripleYielder, RdflibTripleYielder
from rdflib import Graph
from io import StringIO

graph = """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix ex: <http://example.org/stuff/1.0/> .

<http://www.w3.org/TR/rdf-syntax-grammar>
  dc:title "RDF/XML Syntax Specification (Revised)" ;
  ex:editor [
    ex:fullname "Dave Beckett";
    ex:homePage <http://purl.org/net/dajobe/>
  ] ."""

yielder = RdflibParserTripleYielder(raw_graph=graph)
for a_triple in yielder.yield_triples():
    print(a_triple)

print("-------------------")

obj_graph = Graph()
obj_graph.parse(StringIO(graph), format="ttl")

yielder = RdflibTripleYielder(rdflib_graph=obj_graph)
for a_triple in yielder.yield_triples():
    print(a_triple)
