from shexer.core.instances.pconsts import _S, _P, _O


class BaseAnnotator(object):

    def __init__(self, instance_tracker):
        self._instance_tracker = instance_tracker

        # Some short-path to avoid verbosity and too deep references. We'll be gentle with private stuff ;)
        self._all_classes_mode = self._instance_tracker._all_classes_mode
        self._instantiation_property = self._instance_tracker._instantiation_property
        self._subclass_property = self._instance_tracker._subclass_property
        self._instances_dict = self._instance_tracker._instances_dict
        self._classes_considered_in_htree = self._instance_tracker._classes_considered_in_htree
        self._htree = self._instance_tracker._htree

    def is_relevant_triple(self, a_triple):
        if a_triple[_P] != self._instantiation_property:
            return False
        elif self._all_classes_mode:
            if a_triple[_O].iri not in self._instances_dict:
                # The next line "shouldnt" be executed jere, it fits better in annotation methods.
                # However, doing it here avoid to check in those methods again the conditions in which this class
                # should be added to the instnaceS_dict
                self._add_new_class_to_instances_dict(a_triple[_O].iri)
                return True
        elif a_triple[_O].iri not in self._instances_dict:
            return False
        return True

    def anotate_triple(self, a_triple):
        if self._instance_tracker.is_an_instantiation_prop(a_triple[_P]):
            self._anotate_instance(a_triple)


    def _add_new_class_to_instances_dict(self, class_uri):
        self._instances_dict[class_uri] = set()

    def anotation_post_parsing(self):
        pass  # Done! Nothing to do here

    def _anotate_instance(self, a_triple):
        self._instances_dict[a_triple[_O].iri].add(a_triple[_S].iri)


class AnnotatorTrackingInstances(BaseAnnotator):

    def __init__(self, instance_tracker):
        super().__init__(instance_tracker)

    def anotate_triple(self, a_triple):
        if self._instance_tracker.is_subclass_property(a_triple[_P]):
            self._anotate_subclass(a_triple)
        else:
            super().anotate_triple(a_triple)

    def is_relevant_triple(self, a_triple):
        if a_triple[_P] == self._subclass_property:
            return True
        else:
            return super().anotate_triple(a_triple)

    def anotation_post_parsing(self):
        for a_key_class in self._instances_dict:
            self._classes_considered_in_htree.add(a_key_class)
        iri_node = self._htree.iri_node
        for a_key_class in self._classes_considered_in_htree:
            a_class_node = self._get_appropiate_iri_node_and_add_to_htree_if_needed(a_key_class)
            if not a_class_node.has_parents():
                a_class_node.add_parent(iri_node)

    def _get_appropiate_iri_node_and_add_to_htree_if_needed(self, str_iri):
        return self._htree.get_node_of_element(str_iri) if self._htree.contains_element(str_iri) \
            else self._htree.create_node_IRI(str_iri)

    def _anotate_subclass(self, a_triple):
        str_s = str(a_triple[_S])
        str_o = str(a_triple[_O])

        subj_node = self._get_appropiate_iri_node_and_add_to_htree_if_needed(str_s)
        obj_node = self._get_appropiate_iri_node_and_add_to_htree_if_needed(str_o)
        subj_node.add_parent(obj_node)

        self._classes_considered_in_htree.add(str_s)
        self._classes_considered_in_htree.add(str_o)


########################## FUNC

def get_proper_anotator(track_hierarchies, instance_tracker_ref):
    return BaseAnnotator(instance_tracker_ref) if not track_hierarchies \
        else AnnotatorTrackingInstances(instance_tracker_ref)
