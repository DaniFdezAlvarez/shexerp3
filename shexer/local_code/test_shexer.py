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
    
bf:Instance_2 a bf:Instance ; 
    bf:seriesStatement "Department of another stuff" ; 
    bf:seriesEnumeration "8961" ;
    rdfs:label "Cosa wena" ;
    bf:subseriesStatement "General foreign policy series,  1232-5674" ;
    bf:subseriesEnumeration   "volume 311" .

bf:Instance rdfs:subClassOf bf:Concept .
bf:Concept rdfs:subClassOf bf:Class .
"""


namespaces_dict={
"http://id.loc.gov/ontologies/bibframe.rdf/" : "bf",
"http://weso.es/" : "",
"http://www.w3.org/2000/01/rdf-schema#": "rdfs"
}

### raw + all_classes

shaper = Shaper(raw_graph=a_graph,
                all_classes_mode=True,
                input_format=TURTLE,
                namespaces_dict=namespaces_dict)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)

print(result)


### raw + target_classes

print("---------")

target_classes = ["http://id.loc.gov/ontologies/bibframe.rdf/Instance"]

shaper = Shaper(raw_graph=a_graph,
                all_classes_mode=False,
                target_classes=target_classes,
                input_format=TURTLE,
                namespaces_dict=namespaces_dict)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)

print(result)

### raw + selectores
from shexer.consts import FIXED_SHAPE_MAP

raw_shape_map = """

{FOCUS rdfs:subClassOf _}@:a_child
bf:Instance_2@:certain_instance
"""
print("---------")
shaper = Shaper(raw_graph=a_graph,
                all_classes_mode=False,
                target_classes=None,
                input_format=TURTLE,
                shape_map_raw=raw_shape_map,
                shape_map_format=FIXED_SHAPE_MAP,
                namespaces_dict=namespaces_dict)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)

print(result)


### raw + selectors + all_classes

print("---------")
shaper = Shaper(raw_graph=a_graph,
                all_classes_mode=True,
                target_classes=None,
                input_format=TURTLE,
                shape_map_raw=raw_shape_map,
                shape_map_format=FIXED_SHAPE_MAP,
                namespaces_dict=namespaces_dict)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)

print(result)


###################################################  File input

print("------------------------------------------------------------"
      "")

file_graph_name = "files\\test_shexer_graph.ttl"

### raw + all_classes

shaper = Shaper(graph_file_input=file_graph_name,
                all_classes_mode=True,
                input_format=TURTLE,
                namespaces_dict=namespaces_dict)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)

print(result)


### raw + target_classes

print("---------")

target_classes = ["http://id.loc.gov/ontologies/bibframe.rdf/Instance"]

shaper = Shaper(graph_file_input=file_graph_name,
                all_classes_mode=False,
                target_classes=target_classes,
                input_format=TURTLE,
                namespaces_dict=namespaces_dict)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)

print(result)

### raw + selectores
from shexer.consts import FIXED_SHAPE_MAP

raw_shape_map = """

{FOCUS rdfs:subClassOf _}@:a_child
bf:Instance_2@:certain_instance
"""
print("---------")
shaper = Shaper(graph_file_input=file_graph_name,
                all_classes_mode=False,
                target_classes=None,
                input_format=TURTLE,
                shape_map_raw=raw_shape_map,
                shape_map_format=FIXED_SHAPE_MAP,
                namespaces_dict=namespaces_dict)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)

print(result)


### raw + selectors + all_classes

print("---------")
shaper = Shaper(graph_file_input=file_graph_name,
                all_classes_mode=True,
                target_classes=None,
                input_format=TURTLE,
                shape_map_raw=raw_shape_map,
                shape_map_format=FIXED_SHAPE_MAP,
                namespaces_dict=namespaces_dict)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)

print(result)


######################################################### endpoint

### endpoint + target
print("---------")

target_classes = ["http://www.wikidata.org/entity/Q44062313", "http://www.wikidata.org/entity/Q54856362"]
endpoint_url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
instantiation_property = "http://www.wikidata.org/prop/direct/P1344"

shaper = Shaper(all_classes_mode=False,
                target_classes=target_classes,
                url_endpoint=endpoint_url,
                namespaces_dict=namespaces_dict,
                instantiation_property=instantiation_property,
                track_classes_for_entities_at_last_depth_level=False)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)

print(result)


### endpoint + selectors
endpoint_url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
instantiation_property = "http://www.wikidata.org/prop/direct/P31"

raw_shape_map = """

 SPARQL 'SELECT ?s WHERE { ?s <http://www.wikidata.org/prop/direct/P1344> <http://www.wikidata.org/entity/Q44062313> ; <http://www.wikidata.org/prop/direct/P19> <http://www.wikidata.org/entity/Q14317> . }'@:wikifreakoviedo

"""

shaper = Shaper(all_classes_mode=False,
                shape_map_raw=raw_shape_map,
                url_endpoint=endpoint_url,
                namespaces_dict=namespaces_dict,
                instantiation_property=instantiation_property,
                track_classes_for_entities_at_last_depth_level=False)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)
print(result)

## endpoint + selectors + all_clases_mode

endpoint_url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
instantiation_property = "http://www.wikidata.org/prop/direct/P31"

raw_shape_map = """

 SPARQL 'SELECT ?s WHERE { ?s <http://www.wikidata.org/prop/direct/P1344> <http://www.wikidata.org/entity/Q44062313> ; <http://www.wikidata.org/prop/direct/P19> <http://www.wikidata.org/entity/Q14317> . }'@:wikifreakoviedo

"""

shaper = Shaper(all_classes_mode=True,
                shape_map_raw=raw_shape_map,
                url_endpoint=endpoint_url,
                namespaces_dict=namespaces_dict,
                instantiation_property=instantiation_property,
                track_classes_for_entities_at_last_depth_level=False)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)
print(result)


######################################################  input_url

### remote url + all_clases

from shexer.consts import RDF_TYPE, RDF_XML

print("---------")
remote_graph_url = "http://xmlns.com/foaf/spec/index.rdf"
instantiation_property = RDF_TYPE

shaper = Shaper(all_classes_mode=True,
                input_format=RDF_XML,
                url_graph_input=remote_graph_url,
                namespaces_dict=namespaces_dict,
                instantiation_property=instantiation_property)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)
print(result)

### remote_url + target_classes

print("---------")
remote_graph_url = "http://xmlns.com/foaf/spec/index.rdf"
instantiation_property = RDF_TYPE

shaper = Shaper(all_classes_mode=False,
                target_classes=["http://www.w3.org/2002/07/owl#AnnotationProperty" ],
                input_format=RDF_XML,
                url_graph_input=remote_graph_url,
                namespaces_dict=namespaces_dict,
                instantiation_property=instantiation_property)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)
print(result)


### remote_url + selectors

print("---------")
remote_graph_url = "http://xmlns.com/foaf/spec/index.rdf"
instantiation_property = RDF_TYPE

raw_selector = """
{FOCUS  rdfs:isDefinedBy _}@<:soyDenifidoPor>
<http://xmlns.com/foaf/0.1/Project>@<:Proyectico>
"""

shaper = Shaper(all_classes_mode=False,
                shape_map_raw=raw_selector,
                input_format=RDF_XML,
                url_graph_input=remote_graph_url,
                namespaces_dict=namespaces_dict,
                instantiation_property=instantiation_property)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)
print(result)


### remote_url + selectors + all_classes

print("---------")
remote_graph_url = "http://xmlns.com/foaf/spec/index.rdf"
instantiation_property = RDF_TYPE

raw_selector = """
{FOCUS  rdfs:isDefinedBy _}@<:soyDenifidoPor>
<http://xmlns.com/foaf/0.1/Project>@<:Proyectico>
"""

shaper = Shaper(all_classes_mode=True,
                shape_map_raw=raw_selector,
                input_format=RDF_XML,
                url_graph_input=remote_graph_url,
                namespaces_dict=namespaces_dict,
                instantiation_property=instantiation_property)

result = shaper.shex_graph(acceptance_threshold=0.5,
                           string_output=True)
print(result)



