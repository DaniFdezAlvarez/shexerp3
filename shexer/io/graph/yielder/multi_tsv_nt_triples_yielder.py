from shexer.io.graph.yielder.tsv_nt_triples_yielder import TsvNtTriplesYielder
from shexer.io.graph.yielder.multifile_base_triples_yielder import MultifileBaseTripleYielder


class MultiTsvNtTriplesYielder(MultifileBaseTripleYielder):

    def __init__(self, list_of_files, namespaces_to_ignore=None, allow_untyped_numbers=False):
        super(MultiTsvNtTriplesYielder, self).__init__(list_of_files=list_of_files,
                                                       namespaces_to_ignore=namespaces_to_ignore,
                                                       allow_untyped_numbers=allow_untyped_numbers)

    def _constructor_file_yielder(self, a_source_file, parse_namespaces=False):
        return TsvNtTriplesYielder(source_file=a_source_file,
                                   allow_untyped_numbers=self._allow_untyped_numbers,
                                   namespaces_to_ignore=self._namespaces_to_ignore)
