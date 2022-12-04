from django.shortcuts import render
from .forms import TicketForm


def index(request):
    form = TicketForm()
    context = {'form': form}

    return render(request, 'index.html', context)


def review_query(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        data = {
            'form': form
        }

        if not form.is_valid():
            print('Form inválido!')
            return render(request, 'index.html', data)

        return render(request, 'my_query.html', data)
