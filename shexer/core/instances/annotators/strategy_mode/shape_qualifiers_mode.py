from shexer.core.instances.annotators.strategy_mode.base_strategy_mode import BaseStrategyMode
from shexer.utils.triple_yielders import check_if_property_belongs_to_namespace_list
from shexer.utils.shapes import build_shape_name_for_qualifier_prop_uri
from shexer.core.instances.pconsts import _P, _O

class ShapeQualifiersMode(BaseStrategyMode):

    def __init__(self, anotator_ref, namespaces_for_qualifiers_props):
        super().__init__(anotator_ref)
        self._namespaces_for_qualifiers_props = namespaces_for_qualifiers_props
        self._dict_of_qualifier_properties = {}


    def is_relevant_triple(self, a_triple):
        if check_if_property_belongs_to_namespace_list(str_prop=a_triple[_P],
                                                       namespaces=self._namespaces_for_qualifiers_props):
            return True
        return False


    def annotate_triple(self, a_triple):
        self._anotate_qualifier_prop(a_triple[_P])
        self._anotate_instance_of_a_qualifier(a_triple[_O])


    def _anotate_instance_of_a_qualifier(self, a_triple):
        self._instances_dict[self._dict_of_qualifier_properties[a_triple[_P]]].add(a_triple[_O])


    def _anotate_qualifier_prop(self, a_property):
        if a_property not in self._dict_of_qualifier_properties:
            self._dict_of_qualifier_properties[a_property] = build_shape_name_for_qualifier_prop_uri(a_property)
            self._instances_dict[self._dict_of_qualifier_properties[a_property]] = set()


