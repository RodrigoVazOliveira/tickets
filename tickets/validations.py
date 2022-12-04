def origin_and_destination_is_equals(origin, destination, list_errors):
    """ Verificar se origem e destino são iguais """
    if origin == destination:
        list_errors['destination'] = 'Origem e destino não devem ser iguais!'


def input_contains_numbers(value, name_field, list_errors):
    """ Verificar se existe digitos em um cmapo"""
    if any(char.isdigit() for char in value):
        list_errors[name_field] = 'Não inclua digitos'
