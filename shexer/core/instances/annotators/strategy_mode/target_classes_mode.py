
from shexer.core.instances.annotators.strategy_mode.base_strategy_mode import BaseStrategyMode
from shexer.core.instances.pconsts import _P, _O

class TargetClassesMode(BaseStrategyMode):

    def __init__(self, anotator_ref):
        super().__init__(anotator_ref)

    def is_relevant_triple(self, a_triple):
        if a_triple[_P] != self._instantiation_property:
            return False
        if a_triple[_O].iri not in self._instances_dict:
            return False
        return True

    def annotate_triple(self, a_triple):
        if self._instance_tracker.is_an_instantiation_prop(a_triple[_P]):
            self._anotator_ref.annotate_instance(a_triple)


        # if self._instance_tracker.is_an_instantiation_prop(a_triple[_P]):
        #     self._anotate_instance(a_triple)


    # if a_triple[_P] != self._instantiation_property:
#     return False
# elif self._all_classes_mode:
#     if a_triple[_O].iri not in self._instances_dict:
#         # The next line "shouldnt" be executed here, it fits better in annotation methods.
#         # However, doing it here avoid to check in those methods again the conditions in which this class
#         # should be added to the instnaceS_dict
#         self.add_new_class_to_instances_dict(a_triple[_O].iri)
#         return True
# elif a_triple[_O].iri not in self._instances_dict:
#     return False
# return True
