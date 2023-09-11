from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'rooms': 1,
        'cuartos': 2
    }

    return render(request, 'map/index.html', context)