

class ShapeMap(object):

    def __init__(self, shape_map_items=None):
        self._items = shape_map_items if shape_map_items is not None else []


    def add_item(self, shape_map_item):
        self._items.append(shape_map_item)


    def yield_items(self):
        for an_item in self._items:
            yield an_item

class ShapeMapItem(object):

    def __init__(self, node_selector, shape_label):
        self._node_selector = node_selector
        self._shape_label = shape_label