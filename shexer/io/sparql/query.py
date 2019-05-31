from SPARQLWrapper import SPARQLWrapper, JSON


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
    for row in result_query["results"]["bindings"]:
        result.append(row[variable_id]['value'])
    return result

