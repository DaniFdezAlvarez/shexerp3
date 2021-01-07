import unittest
from shexer.shaper import Shaper
from test.const import G1, BASE_FILES, NAMESPACES_WITH_FOAF_AND_EX
from test.t_utils import file_vs_str_tunned_comparison

from rdflib import Graph

from shexer.consts import TURTLE

_BASE_DIR = BASE_FILES + "general\\"

class TestGraphFileInput(unittest.TestCase):

    def test_parsing_file(self):
        a_g = Graph()
        a_g.parse(G1, format="turtle")

        shaper = Shaper(target_classes=["http://xmlns.com/foaf/0.1/Person",
                                        "http://xmlns.com/foaf/0.1/Document"],
                        rdflib_graph=a_g,
                        namespaces_dict=NAMESPACES_WITH_FOAF_AND_EX,
                        all_classes_mode=False,
                        input_format=TURTLE,
                        disable_comments=True)
        str_result = shaper.shex_graph(string_output=True)
        self.assertTrue(file_vs_str_tunned_comparison(file_path=_BASE_DIR + "g1_all_classes_no_comments.shex",
                                                      str_target=str_result))