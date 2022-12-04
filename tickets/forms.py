from datetime import date
from django import forms
from tempus_dominus.widgets import DatePicker
from .travel_class import type_class_travel
from .validations import input_contains_numbers, origin_and_destination_is_equals, \
        date_departure_great_more_date_back, date_departure_minor_date_today


class TicketForm(forms.Form):
    origin = forms.CharField(label='Origem: ', max_length=100)
    destination = forms.CharField(label='Destino: ', max_length=100)
    date_departure = forms.DateField(label='Data de ida: ', widget=DatePicker())
    date_back = forms.DateField(label='Data de volta:', widget=DatePicker())
    date_search = forms.DateField(label='Data de pesquisa:', widget=DatePicker(), disabled=True, initial=date.today())
    travel_class = forms.ChoiceField(label='Tipo de voo', choices=type_class_travel)
    informations = forms.CharField(
        label='Informações extras: ',
        max_length=200,
        required=False,
        widget=forms.Textarea()
    )
    email = forms.EmailField(label='E-mail: ')

    def clean(self):
        list_errors = {}
        origin = self.cleaned_data.get('origin')
        destination = self.cleaned_data.get('destination')
        date_departure = self.cleaned_data.get('date_departure')
        date_back = self.cleaned_data.get('date_back')
        date_search = self.cleaned_data.get('date_search')

        input_contains_numbers(origin, 'origin', list_errors)
        input_contains_numbers(destination, 'destination', list_errors)
        origin_and_destination_is_equals(origin, destination, list_errors)
        date_departure_great_more_date_back(date_departure, date_back, list_errors)
        date_departure_minor_date_today(date_departure, date_search, list_errors)

        self.is_exists_errors(list_errors)

        return self.cleaned_data

    def is_exists_errors(self, list_errors):
        if list_errors is not None:
            for error in list_errors:
                message = list_errors[error]
                self.add_error(error, message)
