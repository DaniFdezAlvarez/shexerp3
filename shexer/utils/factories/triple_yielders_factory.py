from shexer.io.graph.yielder.multi_nt_triples_yielder import MultiNtTriplesYielder
from shexer.io.graph.yielder.nt_triples_yielder import NtTriplesYielder
from shexer.io.graph.yielder.tsv_nt_triples_yielder import TsvNtTriplesYielder
from shexer.io.graph.yielder.multi_tsv_nt_triples_yielder import MultiTsvNtTriplesYielder
from shexer.io.graph.yielder.rdflib_triple_yielder import RdflibTripleYielder
from shexer.io.graph.yielder.multi_rdflib_triple_yielder import MultiRdfLibTripleYielder

from shexer.consts import NT, TSV_SPO, N3, TURTLE, RDF_XML


def get_triple_yielder(source_file=None, list_of_source_files=None, input_format=NT, namespaces_to_ignore=None,
                       allow_untyped_numbers=False, raw_graph=None, namespaces_dict=None, url_input=None,
                       list_of_url_input=None):
    if url_input is not None or list_of_url_input is not None:  # Always use rdflib to parse remote graphs
        if url_input:
            return RdflibTripleYielder(source=url_input,
                                       namespaces_to_ignore=namespaces_to_ignore,
                                       allow_untyped_numbers=allow_untyped_numbers,
                                       raw_graph=raw_graph,
                                       input_format=input_format,
                                       namespaces_dict=namespaces_dict)
        else:  #elif list_of_url_input:
            return MultiRdfLibTripleYielder(list_of_files=list_of_url_input,
                                            namespaces_to_ignore=namespaces_to_ignore,
                                            allow_untyped_numbers=allow_untyped_numbers,
                                            input_format=input_format,
                                            namespaces_dict=namespaces_dict)

    elif input_format == NT:
        if source_file is not None or raw_graph is not None:
            return NtTriplesYielder(source_file=source_file,
                                    namespaces_to_ignore=namespaces_to_ignore,
                                    allow_untyped_numbers=allow_untyped_numbers,
                                    raw_graph=raw_graph)
        else:
            return MultiNtTriplesYielder(list_of_files=list_of_source_files,
                                         namespaces_to_ignore=namespaces_to_ignore,
                                         allow_untyped_numbers=allow_untyped_numbers)
    elif input_format == TSV_SPO:
        if source_file is not None or raw_graph is not None:
            return TsvNtTriplesYielder(source_file=source_file,
                                       namespaces_to_ignore=namespaces_to_ignore,
                                       allow_untyped_numbers=allow_untyped_numbers,
                                       raw_graph=raw_graph)
        else:
            return MultiTsvNtTriplesYielder(list_of_files=list_of_source_files,
                                            namespaces_to_ignore=namespaces_to_ignore,
                                            allow_untyped_numbers=allow_untyped_numbers)
    elif input_format in [TURTLE, N3, RDF_XML]:
        if source_file is not None or raw_graph is not None:
            return RdflibTripleYielder(source=source_file,
                                       namespaces_to_ignore=namespaces_to_ignore,
                                       allow_untyped_numbers=allow_untyped_numbers,
                                       raw_graph=raw_graph,
                                       input_format=input_format,
                                       namespaces_dict=namespaces_dict)
        else:
            return MultiRdfLibTripleYielder(list_of_files=list_of_source_files,
                                            namespaces_to_ignore=namespaces_to_ignore,
                                            allow_untyped_numbers=allow_untyped_numbers,
                                            input_format=input_format,
                                            namespaces_dict=namespaces_dict)


    raise ValueError("Not supported format: " + input_format)
