import json
from shexer.model.statement import Statement
from shexer.model.shape import Shape
from shexer.utils.shapes import build_shapes_name_for_class_uri
from shexer.utils.target_elements import determine_original_target_nodes_if_needed


class ClassShexer(object):

    def __init__(self, class_counts_dict, class_profile_dict=None, class_profile_json_file=None,
                 remove_empty_shapes=True, original_target_classes=None, original_shape_map=None):
        self._class_counts_dict = class_counts_dict
        self._class_profile_dict = class_profile_dict if class_profile_dict is not None else self._load_class_profile_dict_from_file(
            class_profile_json_file)
        self._shapes_list = []
        self._remove_empty_shapes = remove_empty_shapes
        self._original_target_nodes = determine_original_target_nodes_if_needed(remove_empty_shapes=remove_empty_shapes,
                                                                                original_target_classes=original_target_classes,
                                                                                original_shape_map=original_shape_map)

    def shex_classes(self, acceptance_threshold=0):
        self._build_shapes(acceptance_threshold)
        self._clean_shapes()
        self._sort_shapes()

        return self._shapes_list

    def _build_shapes(self, acceptance_threshold):
        for a_class_key in self._class_profile_dict:
            name = build_shapes_name_for_class_uri(a_class_key)
            number_of_instances = float(self._class_counts_dict[a_class_key])
            statements = []
            for a_prop_key in self._class_profile_dict[a_class_key]:
                for a_type_key in self._class_profile_dict[a_class_key][a_prop_key]:
                    for a_cardinality in self._class_profile_dict[a_class_key][a_prop_key][a_type_key]:
                        frequency = self._compute_frequency(number_of_instances,
                                                            self._class_profile_dict
                                                            [a_class_key]
                                                            [a_prop_key]
                                                            [a_type_key]
                                                            [a_cardinality])
                        if frequency >= acceptance_threshold:
                            statements.append(Statement(st_property=a_prop_key,
                                                        st_type=a_type_key,
                                                        cardinality=a_cardinality,
                                                        probability=frequency))

            a_shape = Shape(name=name,
                            class_uri=a_class_key,
                            statements=statements)
            self._shapes_list.append(a_shape)

    def _sort_shapes(self):
        for a_shape in self._shapes_list:
            a_shape.sort_statements(reverse=True,
                                    callback=self._value_to_compare_statements)

    def _clean_shapes(self):

        if not self._remove_empty_shapes:
            return
        shapes_to_remove = self._detect_shapes_to_remove()

        while (len(shapes_to_remove) != 0):
            self._iteration_remove_empty_shapes(shapes_to_remove)
            shapes_to_remove = self._detect_shapes_to_remove()

    def _detect_shapes_to_remove(self):
        result = set()
        for a_shape in self._shapes_list:
            if a_shape.n_statements == 0:
                result.add(a_shape.class_uri)
        return result

    def _iteration_remove_empty_shapes(self, shape_names_to_remove):
        self._remove_shapes_without_statements(shape_names_to_remove)
        self._remove_statements_to_gone_shapes(shape_names_to_remove)

    def _remove_statements_to_gone_shapes(self, shape_names_to_remove):
        for a_shape in self._shapes_list:
            new_statements = []
            for a_statement in a_shape.statements:
                if not a_statement.st_type in shape_names_to_remove:
                    new_statements.append(a_statement)
            a_shape.statements = new_statements

    def _remove_shapes_without_statements(self, shape_names_to_remove):
        new_shape_list = []
        for a_shape in self._shapes_list:
            if not a_shape.name in shape_names_to_remove:
                new_shape_list.append(a_shape)
        self._shapes_list = new_shape_list

    def _value_to_compare_statements(self, a_statement):
        return a_statement.probability

    def _compute_frequency(self, number_of_instances, n_ocurrences_statement):
        return float(n_ocurrences_statement) / number_of_instances

    @staticmethod
    def _load_class_profile_dict_from_file(source_file):
        with open(source_file, "r") as in_stream:
            return json.load(in_stream)
