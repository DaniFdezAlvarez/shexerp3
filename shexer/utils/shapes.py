from shexer.model.shape import STARTING_CHAR_FOR_SHAPE_NAME

def build_shapes_name_for_class_uri(class_uri):
    if "#" in class_uri and class_uri[-1] != "#":
        return STARTING_CHAR_FOR_SHAPE_NAME + class_uri[class_uri.rfind("#") + 1:]
    if "/" in class_uri:
        if class_uri[-1] != "/":
            return STARTING_CHAR_FOR_SHAPE_NAME + class_uri[class_uri.rfind("/") + 1:]
        else:
            return STARTING_CHAR_FOR_SHAPE_NAME + class_uri[class_uri[:-1].rfind("/") + 1:]
    else:
        return class_uri


def build_shape_name_for_qualifier_prop_uri(prop_uri):
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