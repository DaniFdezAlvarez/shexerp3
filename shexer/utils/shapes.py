from shexer.model.shape import STARTING_CHAR_FOR_SHAPE_NAME
from shexer.utils.uri import prefixize_uri_if_possible
from shexer.io.shex.formater.consts import SHAPE_LINK_CHAR

def build_shapes_name_for_class_uri(class_uri, shapes_namespace):
    if class_uri.startswith("<") and class_uri.endswith(">"):
        return STARTING_CHAR_FOR_SHAPE_NAME + class_uri
    last_piece = None
    if "#" in class_uri and class_uri[-1] != "#":
        last_piece = class_uri[class_uri.rfind("#") + 1:]
    if "/" in class_uri:
        if class_uri[-1] != "/":
            last_piece = class_uri[class_uri.rfind("/") + 1:]
        else:
            last_piece = class_uri[class_uri[:-1].rfind("/") + 1:]
    return STARTING_CHAR_FOR_SHAPE_NAME + "<" + shapes_namespace + last_piece + ">" if last_piece is not None else class_uri
        # return class_uri


def build_shape_name_for_qualifier_prop_uri(prop_uri):  # TODO REVIEW!
    result = prop_uri
    if "#" in prop_uri and prop_uri[-1] != "#":
        return STARTING_CHAR_FOR_SHAPE_NAME + prop_uri[prop_uri.rfind("#") + 1:]
    if "/" in prop_uri:
        if prop_uri[-1] != "/":
            return STARTING_CHAR_FOR_SHAPE_NAME + prop_uri[prop_uri.rfind("/") + 1:]
        else:
            return STARTING_CHAR_FOR_SHAPE_NAME + prop_uri[prop_uri[:-1].rfind("/") + 1:]
    else:
        return result.upper()


def prefixize_shape_name_if_possible(a_shape_name, namespaces_prefix_dict):
    result = prefixize_uri_if_possible(target_uri=a_shape_name[1:],                  # Avoid the "@" starting char
                                       namespaces_prefix_dict=namespaces_prefix_dict)
    return result