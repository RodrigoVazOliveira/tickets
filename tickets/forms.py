from datetime import date
from django import forms
from tempus_dominus.widgets import DatePicker
from .travel_class import type_class_travel


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
