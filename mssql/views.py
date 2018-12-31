from django.shortcuts import render, redirect
from django.http import HttpResponse
from mssql.models import *
from inventory.models import *


def index(request):
    categories = {'databaseinventory': databaseinventory,
                  'servermaintenance': servermaintenance}
    return render(request, 'mssql/index.html', context=categories)


def server(request):
    return render(request, 'mssql/server.html')

def serveradd(request):
    return render(request, 'mssql/serveradd.html')