from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Dom - main',
        'content': 'Магазин мебели DOM'
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Dom - about us',
        'content': 'about us',
        'text_on_page': "i belive in you"
    }

    return render(request, 'main/about.html', context)
