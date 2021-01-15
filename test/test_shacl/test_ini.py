import unittest
from shexer.shaper import Shaper
from test.const import G1, BASE_FILES, default_namespaces, G1_ALL_CLASSES_NO_COMMENTS
from shexer.consts import SHACL_TURTLE
# from test.t_utils import file_vs_str_tunned_comparison

from shexer.consts import TURTLE, SHACL_TURTLE

_BASE_DIR = BASE_FILES + "instantiation_prop\\"  # We just need something with another instantiation property


class TestIni(unittest.TestCase):

    def test_all_classes_g1(self):
        shaper = Shaper(
            graph_file_input=G1,
            namespaces_dict=default_namespaces(),
            all_classes_mode=True,
            input_format=TURTLE,
            disable_comments=True)
        str_result = shaper.shex_graph(string_output=False,
                                       output_format=SHACL_TURTLE,
                                       output_file="C:\\Users\\Dani\\repos-git\\shexerp3\\test\\test_shacl\\here.ttl")
        # print(str_result)
        # self.assertTrue(file_vs_str_tunned_comparison(file_path=G1_ALL_CLASSES_NO_COMMENTS,
        #                                               str_target=str_result))