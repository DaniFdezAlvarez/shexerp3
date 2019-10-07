from SPARQLWrapper import SPARQLWrapper, JSON
from urllib.error import HTTPError
from time import sleep

from SPARQLWrapper.SPARQLExceptions import EndPointInternalError

_RESULTS_KEY = "results"
_BINDINGS_KEY = "bindings"
_VALUE_KEY = "value"

def query_endpoint_single_variable(endpoint_url, str_query, variable_id, max_retries=10, sleep_time=5):
    """
    It receives an SPARQL query with a single variable and returns a lit with the resulting nodes

    :param endpoint_url:
    :param str_query:
    :param variable_id:
    :return:
    """
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(str_query)
    sparql.setReturnFormat(JSON)
    last_error = None
    while max_retries > 0:
        try:
            result_query = sparql.query().convert()
            result = []
            for row in result_query[_RESULTS_KEY][_BINDINGS_KEY]:
                result.append(row[variable_id][_VALUE_KEY])
            return result
        except (HTTPError, EndPointInternalError) as e:
            max_retries -= 1
            sleep(sleep_time)
            last_error = e
    last_error.msg = "Max number of attempt reached, it is not possible to perform the query. Msg:\n" + last_error.msg



def query_endpoint_po_of_an_s(endpoint_url, str_query, p_id, o_id, max_retries=5, sleep_time=2):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(str_query)
    sparql.setReturnFormat(JSON)
    last_error = None
    while max_retries > 0:
        try:
            result_query = sparql.query().convert()
            result = []
            for row in result_query[_RESULTS_KEY][_BINDINGS_KEY]:
                p_value = row[p_id][_VALUE_KEY]
                o_value = row[o_id][_VALUE_KEY]
                result.append((p_value, o_value))
            return result
        except (HTTPError, EndPointInternalError) as e:
            max_retries -= 1
            sleep(sleep_time)
            last_error = e
    last_error.msg = "Max number of attempt reached, it is not possible to perform the query. Msg:\n" + last_error.msg