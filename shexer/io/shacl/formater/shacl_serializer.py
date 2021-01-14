from shexer.core.class_profiler import RDF_TYPE_STR
from shexer.model.shape import STARTING_CHAR_FOR_SHAPE_NAME
from rdflib import Graph, Namespace, URIRef, RDF, BNode

_EXPECTED_SHAPE_BEGINING = STARTING_CHAR_FOR_SHAPE_NAME + "<"
_EXPECTED_SHAPE_ENDING = ">"

_SHACL_NAMESPACE = "http://www.w3.org/ns/shacl#"

_SHACL_PRIORITY_PREFIXES = ["sh", "shacl", "sha"]

_R_SHACL_SHAPE_URI = URIRef(_SHACL_NAMESPACE + "NodeShape")
_R_SHACL_TARGET_CLASS_PROP = URIRef(_SHACL_NAMESPACE + "targetClass")

_R_SHACL_PROPERTY_PROP = URIRef(_SHACL_NAMESPACE + "targetClass")


class ShaclSerializer(object):

    def __init__(self, target_file, shapes_list, namespaces_dict=None, string_return=False,
                 instantiation_property_str=RDF_TYPE_STR):
        self._target_file = target_file
        self._namespaces_dict = namespaces_dict if namespaces_dict is not None else {}
        self._shapes_list = shapes_list
        self._string_return = string_return
        self._instantiation_property_str = instantiation_property_str

        self._g_shapes = Graph()

    def serialize_shapes(self):
        self._add_namespaces()
        self._add_shapes()
        return self._produce_output()

    #################### NAMESPACES

    def _add_namespaces(self):
        self._add_param_namespaces()
        self._add_shacl_namespace_if_needed()

    def _add_param_namespaces(self):
        for a_namespace, a_prefix in self._namespaces_dict:
            self._add_namespace(prefix=a_prefix,
                                namespace_str=a_namespace)

    def _add_namespace(self, prefix, namespace_str):
        self._g_shapes.bind(prefix=prefix,
                            namespace=Namespace(namespace_str))

    def _add_shacl_namespace_if_needed(self):
        if _SHACL_NAMESPACE in self._namespaces_dict:  # shacl already included
            return
        curr_prefixes = self._namespaces_dict.values()
        for a_prefix in _SHACL_PRIORITY_PREFIXES:  # trying default prefixes
            if a_prefix not in curr_prefixes:
                self._add_shacl_namespace(a_prefix)
                return
        counter = 1  # going for random prefixes, no defs. available
        candidate_pref = _SHACL_PRIORITY_PREFIXES[0] + str(counter)
        while candidate_pref in curr_prefixes:
            counter += 1
            candidate_pref = _SHACL_PRIORITY_PREFIXES[0] + str(counter)
        self._add_shacl_namespace(candidate_pref)

    def _add_shacl_namespace(self, shacl_prefix):
        self._add_namespace(prefix=shacl_prefix,
                            namespace_str=_SHACL_NAMESPACE)
        self._namespaces_dict[_SHACL_NAMESPACE] = shacl_prefix

    #################### SHAPES

    def _add_shapes(self):
        for a_shape in self._shapes_list:
            self._add_shape(a_shape)

    def _add_shape(self, shape):
        r_shape_uri = self._generate_shape_uri(shape=shape)
        self._add_shape_uri(r_shape_uri=r_shape_uri)
        self._add_target_class(r_shape_uri=r_shape_uri,
                               shape=shape)
        self._add_shape_constraints(shape=shape,
                                    r_shape_uri=r_shape_uri)

    def _add_target_class(self, shape, r_shape_uri):
        if shape.class_uri is not None:
            self._add_triple(r_shape_uri,
                             _R_SHACL_TARGET_CLASS_PROP,
                             URIRef(shape.class_uri))  # TODO check if this is alway an abs. URI, not sure

    def _add_shape_constraints(self, shape, r_shape_uri):
        for a_statement in shape.yield_statements():
            self._add_constraint(statement=a_statement,
                                 r_shape_uri=r_shape_uri)

    def _add_constraint(self, statement, r_shape_uri):
        r_constraint_node = self._generate_bnode()
        self._add_bnode_property(r_shape_uri=r_shape_uri,
                                 r_constraint_node=r_constraint_node)
        self._add_path(r_shape_uri=r_shape_uri,
                       statement=statement,
                       r_constraint_node=r_constraint_node)
        self._add_node_type(r_shape_uri=r_shape_uri,
                            statement=statement,
                            r_constraint_node=r_constraint_node)
        self._add_cardinality(r_shape_uri=r_shape_uri,
                              statement=statement,
                              r_constraint_node=r_constraint_node)

    def _add_path(self, r_shape_uri, statement, r_constraint_node):
        pass  # TODO

    def _add_node_type(self, r_shape_uri, statement, r_constraint_node):
        pass  # TODO

    def _add_cardinality(self, r_shape_uri, statement, r_constraint_node):
        pass  # TODO


    def _add_bnode_property(self, r_shape_uri, r_constraint_node):
        self._add_triple(r_shape_uri, _R_SHACL_PROPERTY_PROP, r_constraint_node)

    def _generate_shape_uri(self, shape):
        if shape.name.startswith(_EXPECTED_SHAPE_BEGINING) and shape.name.endswith(_EXPECTED_SHAPE_ENDING):
            return URIRef(shape.name[2:-1])  # Excluding  "@<"  and ">

    def _add_shape_uri(self, r_shape_uri):
        self._add_triple(r_shape_uri, RDF.type, _R_SHACL_SHAPE_URI)

    def _add_triple(self, s, p, o):
        self._g_shapes.add((s, p, o))

    @staticmethod
    def _generate_bnode():
        return BNode()

    #################### OUTPUT

    def _produce_output(self):
        pass  # TODO
