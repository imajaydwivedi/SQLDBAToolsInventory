from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me': 'Hello, I am from inventory/views.py!'}
    return render(request, 'inventory/index.html', context=my_dict)
