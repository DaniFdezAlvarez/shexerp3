from SPARQLWrapper import SPARQLWrapper, JSON


_RESULTS_KEY = "results"
_BINDINGS_KEY = "bindings"
_VALUE_KEY = "value"

def query_endpoint_single_variable(endpoint_url, str_query, variable_id):
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
    result_query = sparql.query().convert()
    result = []
    for row in result_query[_RESULTS_KEY][_BINDINGS_KEY]:
        result.append(row[variable_id][_VALUE_KEY])
    return result


def query_endpoint_po_of_an_s(endpoint_url, str_query, p_id, o_id):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(str_query)
    sparql.setReturnFormat(JSON)
    result_query = sparql.query().convert()
    result = []
    for row in result_query[_RESULTS_KEY][_BINDINGS_KEY]:
        p_value = row[p_id][_VALUE_KEY]
        o_value = row[o_id][_VALUE_KEY]
        result.append((p_value, o_value))
    return result