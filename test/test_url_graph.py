import unittest
from shexer.shaper import Shaper
from test.const import BASE_FILES, NAMESPACES_WITH_FOAF_AND_EX
from test.t_utils import file_vs_str_tunned_comparison

from shexer.consts import NT, TURTLE

_BASE_DIR = BASE_FILES + "general\\"

class TestUrlGraphFormat(unittest.TestCase):

    def test_ttl(self):
        shaper = Shaper(target_classes=["http://xmlns.com/foaf/0.1/Person",
                                        "http://xmlns.com/foaf/0.1/Document"],
                        url_graph_input="https://raw.githubusercontent.com/DaniFdezAlvarez/shexerp3/develop/test/t_files/t_graph_1.ttl",
                        namespaces_dict=NAMESPACES_WITH_FOAF_AND_EX,
                        all_classes_mode=False,
                        input_format=TURTLE,
                        disable_comments=True)
        str_result = shaper.shex_graph(string_output=True)
        self.assertTrue(file_vs_str_tunned_comparison(file_path=_BASE_DIR + "g1_all_classes_no_comments.shex",
                                                      str_target=str_result))


    def test_nt(self):
        shaper = Shaper(target_classes=["http://xmlns.com/foaf/0.1/Person",
                                        "http://xmlns.com/foaf/0.1/Document"],
                        url_graph_input="https://raw.githubusercontent.com/DaniFdezAlvarez/shexerp3/develop/test/t_files/t_graph_1.nt",
                        namespaces_dict=NAMESPACES_WITH_FOAF_AND_EX,
                        all_classes_mode=False,
                        input_format=NT,
                        disable_comments=True)
        str_result = shaper.shex_graph(string_output=True)
        self.assertTrue(file_vs_str_tunned_comparison(file_path=_BASE_DIR + "g1_all_classes_no_comments.shex",
                                                      str_target=str_result))


