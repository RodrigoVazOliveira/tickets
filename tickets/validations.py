def origin_and_destination_is_equals(origin, destination, list_errors):
    """ Verificar se origem e destino são iguais """
    if origin == destination:
        list_errors['destination'] = 'Origem e destino não devem ser iguais!'


def input_contains_numbers(value, name_field, list_errors):
    """ Verificar se existe digitos em um cmapo"""
    if any(char.isdigit() for char in value):
        list_errors[name_field] = 'Não inclua digitos'


def date_departure_great_more_date_back(date_departure, date_back, list_errors):
    """ Verificar se data de ida é maior que a data de volta """
    if date_departure > date_back:
        list_errors['date_departure'] = 'Data de ida não pode ser maior que a data de volta!'


def date_departure_minor_date_today(date_departure, date_search, list_errors):
    """ Verificar se data de ida é menor que a data da pesquisa (hoje) """
    if date_departure < date_search:
        list_errors['date_departure'] = 'Data de ida não pode ser menor que a data de pesquisa!'