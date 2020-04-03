from shexer.utils.factories.triple_yielders_factory import produce_shape_map_according_to_input


def get_shape_map_if_needed(sm_format, sgraph, namespaces_prefix_dict, target_classes,
                            file_target_classes, shape_map_file, shape_map_raw,
                            instantiation_property, shape_map_already_built=None):
    if shape_map_file is None and shape_map_raw is None:
        return None
    return produce_shape_map_according_to_input(sm_format=sm_format,
                                                sgraph=sgraph,
                                                namespaces_prefix_dict=namespaces_prefix_dict,
                                                target_classes=target_classes,
                                                file_target_classes=file_target_classes,
                                                shape_map_file=shape_map_file,
                                                shape_map_raw=shape_map_raw,
                                                instantiation_property=instantiation_property,
                                                shape_map_already_built=shape_map_already_built)