import unittest
from shexer.shaper import Shaper
from test.const import G1, BASE_FILES, G1_NT, NAMESPACES_WITH_FOAF_AND_EX
from test.t_utils import file_vs_str_tunned_comparison

from shexer.consts import TURTLE

_BASE_DIR = BASE_FILES + "general\\"

class TestGraphFileInput(unittest.TestCase):

    def test_some_format(self):
        shaper = Shaper(target_classes=["http://xmlns.com/foaf/0.1/Person",
                                        "http://xmlns.com/foaf/0.1/Document"],
                        graph_file_input=G1,
                        namespaces_dict=NAMESPACES_WITH_FOAF_AND_EX,
                        all_classes_mode=False,
                        input_format=TURTLE,
                        disable_comments=True)
        str_result = shaper.shex_graph(string_output=True)
        self.assertTrue(file_vs_str_tunned_comparison(file_path=_BASE_DIR + "g1_all_classes_no_comments.shex",
                                                      str_target=str_result))


    def test_no_format(self):  # Should be nt
        shaper = Shaper(target_classes=["http://xmlns.com/foaf/0.1/Person",
                                        "http://xmlns.com/foaf/0.1/Document"],
                        graph_file_input=G1_NT,
                        namespaces_dict=NAMESPACES_WITH_FOAF_AND_EX,
                        all_classes_mode=False,
                        disable_comments=True)
        str_result = shaper.shex_graph(string_output=True)
        self.assertTrue(file_vs_str_tunned_comparison(file_path=_BASE_DIR + "g1_all_classes_no_comments.shex",
                                                      str_target=str_result))