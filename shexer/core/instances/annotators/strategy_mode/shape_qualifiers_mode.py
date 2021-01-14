from shexer.core.instances.annotators.strategy_mode.base_strategy_mode import BaseStrategyMode
from shexer.utils.triple_yielders import check_if_property_belongs_to_namespace_list
from shexer.utils.shapes import build_shape_name_for_qualifier_prop_uri
from shexer.core.instances.pconsts import _P, _O

class ShapeQualifiersMode(BaseStrategyMode):

    def __init__(self, annotator_ref, namespaces_for_qualifiers_props, shapes_namespace):
        super().__init__(annotator_ref)
        self._namespaces_for_qualifiers_props = namespaces_for_qualifiers_props
        self._dict_of_qualifier_properties = {}
        self._shapes_namespace = shapes_namespace


    def is_relevant_triple(self, a_triple):
        if check_if_property_belongs_to_namespace_list(str_prop=a_triple[_P].iri,
                                                       namespaces=self._namespaces_for_qualifiers_props):
            return True
        return False


    def annotate_triple(self, a_triple):
        self._annotate_qualifier_prop(a_triple[_P])
        self._annotate_instance_of_a_qualifier(a_triple)


    def _annotate_instance_of_a_qualifier(self, a_triple):
        self._instances_dict[self._dict_of_qualifier_properties[a_triple[_P].iri]].add(a_triple[_O].iri)


    def _annotate_qualifier_prop(self, a_property):
        str_prop = a_property.iri
        if str_prop not in self._dict_of_qualifier_properties:
            self._dict_of_qualifier_properties[str_prop] = \
                build_shape_name_for_qualifier_prop_uri(prop_uri=str_prop,
                                                        shapes_namespace=self._shapes_namespace)
            self._instances_dict[self._dict_of_qualifier_properties[str_prop]] = set()

    # def annotation_post_parsing(self):
        # for a_key in self._dict_of_qualifier_properties:
        #
        #     prop_shape_name = self._dict_of_qualifier_properties[a_key]
        #     # print(prop_shape_name, a_key)
        #     if len(self._instances_dict[prop_shape_name]) == 0:
        #         print("Gone!", prop_shape_name)
        #         del self._instances_dict[prop_shape_name]
        #     else:
        #         print(prop_shape_name, self._instances_dict[prop_shape_name])


