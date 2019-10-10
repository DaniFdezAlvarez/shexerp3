class ShapeMapLabelParser(object):

    def __init__(self, prefix_namespaces_dict=None):
        self._namespaces_prefix_dict = prefix_namespaces_dict if prefix_namespaces_dict is not None else {}

    def parse_shape_map_label(self, raw_label):
        if self._is_a_prefixed_uri(raw_label):
            return self._parse_prefixed_label(raw_label)
        return self._parse_unprefixed_label(raw_label)


    def _is_a_prefixed_uri(self, raw_label):
        # print(raw_label, raw_label.startswith("<"), raw_label.endswith(">"))
        if len(raw_label) < 2:
            return False
        if raw_label.startswith("<") and raw_label.endswith(">"):
            return False
        return True


    def _parse_unprefixed_label(self, raw_label):
        return raw_label[1:-1]

    def _parse_prefixed_label(self, raw_label):
        index_sep = raw_label.find(":")
        if index_sep == -1:
            raise ValueError("Wrong label: expecting a URI surrounded by <> or a prefixed element: " + raw_label)
        target_prefix = raw_label[:index_sep]
        if target_prefix in self._namespaces_prefix_dict:
            return self._namespaces_prefix_dict[target_prefix] + raw_label[index_sep + 1:]
        else:
            raise ValueError("Unknown prefix in label: " + raw_label)




