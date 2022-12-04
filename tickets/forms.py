from datetime import date
from django import forms
from tempus_dominus.widgets import DatePicker


class TicketForm(forms.Form):
    origin = forms.CharField(label='Origem: ', max_length=100)
    destination = forms.CharField(label='Destino: ', max_length=100)
    date_departure = forms.DateField(label='Data de ida: ', widget=DatePicker())
    date_back = forms.DateField(label='Data de volta:', widget=DatePicker())
