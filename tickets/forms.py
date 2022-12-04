from datetime import date
from django import forms
from tempus_dominus.widgets import DatePicker
from .travel_class import type_class_travel
from .validations import input_contains_numbers, origin_and_destination_is_equals

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
        origin = self.cleaned_data.get('origin')
        destination = self.cleaned_data.get('destination')
        list_errors = {}

        input_contains_numbers(origin, 'origin', list_errors)
        input_contains_numbers(destination, 'destination', list_errors)
        origin_and_destination_is_equals(origin, destination, list_errors)

        self.is_exists_errors(list_errors)

        return self.cleaned_data

    def is_exists_errors(self, list_errors):
        if list_errors is not None:
            for error in list_errors:
                message = list_errors[error]
                self.add_error(error, message)
