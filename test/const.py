BASE_FILES = "C:\\Users\\Dani\\repos-git\\shexerp3\\test\\files\\"

G1 = BASE_FILES + "t_graph_1.ttl"
G1_NT = BASE_FILES + "t_graph_1.nt"
G1_TSVO_SPO = BASE_FILES + "t_graph_1.tsv"
G1_JSON_LD = BASE_FILES + "t_graph_1.json"
G1_XML = BASE_FILES + "t_graph_1.xml"
G1_N3 = BASE_FILES + "t_graph_1.n3"


# PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX foaf: <http://xmlns.com/foaf/0.1/>

NAMESPACES_WITH_FOAF_AND_EX = {"http://example.org/" : "ex",
                               "http://www.w3.org/XML/1998/namespace/" : "xml",
                               "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                               "http://www.w3.org/2000/01/rdf-schema#" : "rdfs",
                               "http://www.w3.org/2001/XMLSchema#": "xsd",
                               "http://xmlns.com/foaf/0.1/": "foaf"
                               }