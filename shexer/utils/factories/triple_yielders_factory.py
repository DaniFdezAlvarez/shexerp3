from shexer.io.graph.yielder.multi_nt_triples_yielder import MultiNtTriplesYielder
from shexer.io.graph.yielder.nt_triples_yielder import NtTriplesYielder
from shexer.io.graph.yielder.tsv_nt_triples_yielder import TsvNtTriplesYielder
from shexer.io.graph.yielder.multi_tsv_nt_triples_yielder import MultiTsvNtTriplesYielder
from shexer.io.graph.yielder.rdflib_triple_yielder import RdflibTripleYielder
from shexer.io.graph.yielder.multi_rdflib_triple_yielder import MultiRdfLibTripleYielder
from shexer.io.graph.yielder.remote.sgraph_from_selectors_triple_yielder import SgraphFromSelectorsTripleYielder
from shexer.io.graph.yielder.filter.filter_namespaces_triple_yielder import FilterNamespacesTriplesYielder
from shexer.utils.factories.shape_map_parser_factory import get_shape_map_parser
from shexer.model.graph.endpoint_sgraph import EndpointSGraph

from shexer.consts import NT, TSV_SPO, N3, TURTLE, RDF_XML, FIXED_SHAPE_MAP


def get_triple_yielder(source_file=None, list_of_source_files=None, input_format=NT, namespaces_to_ignore=None,
                       allow_untyped_numbers=False, raw_graph=None, namespaces_dict=None, url_input=None,
                       list_of_url_input=None, shape_map_file=None, shape_map_raw=None, shape_map_format=FIXED_SHAPE_MAP,
                       track_classes_for_entities_at_last_depth_level=True,
                       depth_for_building_subgraph=1, url_endpoint=None,
                       instantiation_property=None,
                       strict_syntax_with_corners=False):
    result = None
    if url_endpoint is not None:
        sgrpah=EndpointSGraph(endpoint_url=url_endpoint)
        shape_map_parser = get_shape_map_parser(format=shape_map_format,
                                                sgraph=sgrpah,
                                                namespaces_prefix_dict=namespaces_dict)

        s_map = shape_map_parser.parse_shape_map(source_file=shape_map_file,
                                                 raw_content=shape_map_raw)

        result = SgraphFromSelectorsTripleYielder(shape_map=s_map,
                                                  depth=depth_for_building_subgraph,
                                                  classes_at_last_level=track_classes_for_entities_at_last_depth_level,
                                                  instantiation_property=instantiation_property,
                                                  strict_syntax_with_corners=strict_syntax_with_corners,
                                                  allow_untyped_numbers=allow_untyped_numbers
                                                  )
    elif url_input is not None or list_of_url_input is not None:  # Always use rdflib to parse remote graphs
        if url_input:
            result = RdflibTripleYielder(source=url_input,
                                         allow_untyped_numbers=allow_untyped_numbers,
                                         raw_graph=raw_graph,
                                         input_format=input_format,
                                         namespaces_dict=namespaces_dict)
        else:  # elif list_of_url_input:
            result = MultiRdfLibTripleYielder(list_of_files=list_of_url_input,
                                              allow_untyped_numbers=allow_untyped_numbers,
                                              input_format=input_format,
                                              namespaces_dict=namespaces_dict)

    elif input_format == NT:
        if source_file is not None or raw_graph is not None:
            result = NtTriplesYielder(source_file=source_file,
                                      allow_untyped_numbers=allow_untyped_numbers,
                                      raw_graph=raw_graph)
        else:
            result = MultiNtTriplesYielder(list_of_files=list_of_source_files,
                                           allow_untyped_numbers=allow_untyped_numbers)
    elif input_format == TSV_SPO:
        if source_file is not None or raw_graph is not None:
            result = TsvNtTriplesYielder(source_file=source_file,
                                         allow_untyped_numbers=allow_untyped_numbers,
                                         raw_graph=raw_graph)
        else:
            result = MultiTsvNtTriplesYielder(list_of_files=list_of_source_files,
                                              allow_untyped_numbers=allow_untyped_numbers)
    elif input_format in [TURTLE, N3, RDF_XML]:
        if source_file is not None or raw_graph is not None:
            result = RdflibTripleYielder(source=source_file,
                                         allow_untyped_numbers=allow_untyped_numbers,
                                         raw_graph=raw_graph,
                                         input_format=input_format,
                                         namespaces_dict=namespaces_dict)
        else:
            result = MultiRdfLibTripleYielder(list_of_files=list_of_source_files,
                                              allow_untyped_numbers=allow_untyped_numbers,
                                              input_format=input_format,
                                              namespaces_dict=namespaces_dict)

    else:
        raise ValueError("Not supported format: " + input_format)

    if namespaces_to_ignore is None:
        return result
    else:
        return FilterNamespacesTriplesYielder(actual_triple_yielder=result,
                                              namespaces_to_ignore=namespaces_to_ignore)
