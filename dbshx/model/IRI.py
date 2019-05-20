from dbshx.model.const_elem_types import IRI_ELEM_TYPE


class IRI(object):

    def __init__(self, content):
        self._content = content

    def __str__(self):
        return self._content

    @property
    def elem_type(self):
        return IRI_ELEM_TYPE

    @property
    def iri(self):
        return self._content

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)