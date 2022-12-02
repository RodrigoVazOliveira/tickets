from django.shortcuts import render
from .forms import TicketForm


def index(request):
    form = TicketForm()
    context = {'form' : form}

    return render(request, 'index.html', context)