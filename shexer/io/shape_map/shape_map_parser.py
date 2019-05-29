from shexer.utils.file import load_whole_file_content
from shexer.model.shape_map import ShapeMap, ShapeMapItem
from shexer.io.shape_map.node_selector.node_selector_parser import NodeSelectorParser

class ShapeMapParser(object):

    def __init__(self, namespaces_prefix_dict):
        self._node_selector_parser = NodeSelectorParser(namespaces_prefix_dict=namespaces_prefix_dict)

    def parse_shape_map(self, source_file=None, raw_content=None):
        self._check_input(source_file, raw_content)
        target_content = raw_content
        if source_file is not None:
            target_content = load_whole_file_content(source_file)
        return self._parse_shape_map_from_str(target_content)

    @staticmethod
    def _check_input(source_file, raw_content):
        if (source_file is None) == (raw_content is None):
            raise ValueError("Yoy must provide exactly one kind of input")

    def _parse_shape_map_from_str(self, raw_content):
        raise NotImplementedError("Implement this in derived classes")


####################################################

import json

_KEY_NODE_SELECTOR = "nodeSelector"
_KEY_LABEL = "shapeLabel"



class JsonShapeMapParser(ShapeMapParser):
    """
    Example of expected format:
    [
  { "nodeSelector": "<http://data.example/node1>,
    "shapeLabel": "<http://schema.example/Shape2>
    },
  { "nodeSelector": "<http://data.example/node1>,
    "shapeLabel": "<http://schema.example/Shape2>
    }
]
    """

    def __init__(self, namespaces_prefix_dict):
        super().__init__(namespaces_prefix_dict)

    def _parse_shape_map_from_str(self, raw_content):
        result = ShapeMap()
        json_obj = json.loads(raw_content)
        for a_list_elem in json_obj:
            result.add_item(ShapeMapItem(node_selector=self._node_selector_parser.parse_node_selector(a_list_elem[_KEY_NODE_SELECTOR]),
                                         shape_label=a_list_elem[_KEY_LABEL]))
        return result

