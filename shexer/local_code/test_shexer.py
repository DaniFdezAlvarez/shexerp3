from shexer.shaper import Shaper
from shexer.consts import TURTLE

a_graph = """
@base <http://library.edu/> . 
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> . 
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . 
@prefix bf: <http://id.loc.gov/ontologies/bibframe.rdf/> . 

<Instance_1> a bf:Instance ; 
    bf:seriesStatement "Department of State publication" ; 
    bf:seriesEnumeration "8961" ;
    bf:subseriesStatement "General foreign policy series,  9876-5432" ;
    bf:subseriesEnumeration   "volume 310" .

bf:Instance rdfs:subClassOf bf:Concept .
bf:Concept rdfs:subClassOf bf:Class .
"""


namespaces_dict={
}

shaper = Shaper(raw_graph=a_graph,
                all_classes_mode=True,
                input_format=TURTLE,
                namespaces_dict=namespaces_dict)

result = shaper.shex_graph(aceptance_threshold=0.5,
                           string_output=True)

htree = shaper._instance_tracker.htree
# print(htree.iri_node._children)
# print(htree.get_node_of_element("http://id.loc.gov/ontologies/bibframe.rdf/Class")._children)
# print(htree.get_node_of_element("http://id.loc.gov/ontologies/bibframe.rdf/Class")._parents)
# print(htree.get_node_of_element('http://id.loc.gov/ontologies/bibframe.rdf/Concept')._children)


print(result)
