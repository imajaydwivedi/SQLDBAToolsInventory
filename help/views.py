from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dict = {'insert_me': 'Hello, I am being called from help/views.py!'}
    return render(request, 'help/index.html', my_dict)
