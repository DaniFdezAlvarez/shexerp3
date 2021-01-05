import unittest
from shexer.shaper import Shaper
from test.const import G1, BASE_FILES, G1_NT, NAMESPACES_WITH_FOAF_AND_EX, G1_ALL_CLASSES_NO_COMMENTS
from test.t_utils import file_vs_str_tunned_comparison

from shexer.consts import NT

_BASE_DIR = BASE_FILES + "untyped_numbers\\"

class TestInferNumericTypesForUntypedLiterals(unittest.TestCase):

    def test_some_format(self):
        shaper = Shaper(target_classes=["http://xmlns.com/foaf/0.1/Person",
                                        "http://xmlns.com/foaf/0.1/Document"],
                        graph_file_input=_BASE_DIR + "g1_untyped_age.nt",
                        namespaces_dict=NAMESPACES_WITH_FOAF_AND_EX,
                        all_classes_mode=False,
                        infer_numeric_types_for_untyped_literals=True,
                        input_format=NT,
                        disable_comments=True)
        str_result = shaper.shex_graph(string_output=True)
        print(str_result)
        self.assertTrue(file_vs_str_tunned_comparison(file_path=G1_ALL_CLASSES_NO_COMMENTS,
                                                      str_target=str_result))