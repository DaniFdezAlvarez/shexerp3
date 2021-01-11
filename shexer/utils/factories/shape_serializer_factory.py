from shexer.consts import SHEX
from shexer.io.shex.formater.shex_serializer import ShexSerializer


def get_shape_serializer(output_format, shapes_list, target_file=None, string_return=False, namespaces_dict=None,
                         tolerance_to_keep_similar_rules=0.15, keep_less_specific=True,
                         instantiation_property=None, discard_useless_constraints_with_positive_closure=True,
                         all_compliant_mode=True, disable_comments=False, disable_or_statements=True):
    if output_format == SHEX:
        return ShexSerializer(target_file=target_file,
                              shapes_list=shapes_list,
                              namespaces_dict=namespaces_dict,
                              tolerance_to_keep_similar_rules=tolerance_to_keep_similar_rules,
                              keep_less_specific=keep_less_specific,
                              string_return=string_return,
                              instantiation_property_str=instantiation_property,
                              discard_useless_positive_closures=discard_useless_constraints_with_positive_closure,
                              all_compliant_mode=all_compliant_mode,
                              disable_comments=disable_comments,
                              disable_or_statements=disable_or_statements)
    else:
        raise ValueError("Currently unsupported format: " + output_format)
