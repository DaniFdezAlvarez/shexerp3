from shexer.shaper import Shaper
from shexer.consts import TURTLE

a_graph = """
@prefix : <http://example.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:Marie a :person ;
	:likes :Justine ;
	:likes :Antoine ;
	:likes :football ;
	:name "Marie" ;
	:age "30"^^xsd:int .

:Justine a :person ;
    :likes :Marie ;
    :likes :basketball ;
    :name "Justine" .

:Antoine a :person ;
	:likes :Marie ;
	:likes :Justine ;
	:name "Antoine" ;
	:age "32"^^xsd:int .
"""

shaper = Shaper(all_classes_mode=True,
                raw_graph=a_graph,
                input_format=TURTLE)
resutl = shaper.profile_graph(string_output=True)
print(resutl)