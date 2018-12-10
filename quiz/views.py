from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  my_dict = {'insert_me':'Hello, I am from quiz/view.py!'}
  return render(request, 'quiz/index.html', my_dict)
  # return HttpResponse("Welcome to TiVo SQL Inventory Quiz Page.")
