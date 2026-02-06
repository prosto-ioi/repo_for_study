from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'home',
        'content': 'Shop main page - Home',
        'list': ['firs', 'second'],
        'dict': {'first': 1},
        'is_authenticated': 1
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')
