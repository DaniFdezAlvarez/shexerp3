from shexer.core.class_shexer import ClassShexer


def get_class_shexer(class_instances_target_dict,
                     class_profile_dict,
                     remove_empty_shapes,
                     original_target_classes,
                     original_shape_map):
    class_count_dicts = {}

    for a_class_key in class_instances_target_dict:
        class_count_dicts[a_class_key] = len(class_instances_target_dict[a_class_key])

    return ClassShexer(
        class_counts_dict=class_count_dicts,
        class_profile_dict=class_profile_dict,
        class_profile_json_file=None,
        remove_empty_shapes=remove_empty_shapes,
        original_target_classes=original_target_classes,
        original_shape_map=original_shape_map
    )