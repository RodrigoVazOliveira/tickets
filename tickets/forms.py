from django import forms


class TicketForm(forms.Form):
    origin = forms.CharField(label='origin', max_length=100)
    destination = forms.CharField(label='destination', max_length=100)
    date_departure = forms.DateField(label='date_departure')
    date_back = forms.DateField(label='date_back')
