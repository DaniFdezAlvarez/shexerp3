import unittest
from shexer.shaper import Shaper
from test.const import BASE_FILES
from test.t_utils import file_vs_str_tunned_comparison

_BASE_DIR = BASE_FILES + "wikidata_annotation\\"

class TestWikidataAnnotation(unittest.TestCase):

    def test_no_annotation(self):
        shaper = Shaper(all_classes_mode=True,
                        graph_file_input=_BASE_DIR + "wiki_example.ttl",
                        instantiation_property="http://www.wikidata.org/prop/direct/P31",
                        input_format="turtle",
                        disable_comments=True,
                        )
        str_result = shaper.shex_graph(string_output=True)
        self.assertTrue(file_vs_str_tunned_comparison(file_path=_BASE_DIR + "wiki_example_noanot.shex",
                                                      str_target=str_result))

    def test_annotation(self):
        shaper = Shaper(all_classes_mode=True,
                        graph_file_input=_BASE_DIR + "wiki_example.ttl",
                        instantiation_property="http://www.wikidata.org/prop/direct/P31",
                        input_format="turtle",
                        disable_comments=True,
                        wikidata_annotation=True
                        )
        str_result = shaper.shex_graph(string_output=True)
        print(str_result)
        self.assertTrue(file_vs_str_tunned_comparison(file_path=_BASE_DIR + "wiki_example_noanot.shex",
                                                      str_target=str_result))
