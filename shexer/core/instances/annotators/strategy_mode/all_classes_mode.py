from shexer.core.instances.annotators.strategy_mode.base_strategy_mode import BaseStrategyMode
from shexer.core.instances.pconsts import _S, _P, _O

class AllClasesMode(BaseStrategyMode):

    def __init__(self, anotator_ref):
        super().__init__(anotator_ref)



    def is_relevant_triple(self, a_triple):
        if a_triple[_P] != self._instantiation_property:
            return False
        return True


    def annotate_triple(self, a_triple):
        if self._instance_tracker.is_an_instantiation_prop(a_triple[_P]):
            self._anotator_ref.add_new_class_to_instances_dict(a_triple[_O].iri)
            self._anotator_ref.anotate_instance(a_triple)


