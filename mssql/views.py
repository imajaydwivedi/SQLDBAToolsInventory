from django.shortcuts import render, redirect
from django.http import HttpResponse
from mssql.models import *
#from inventory.models import *
from django.db import connection
from SQLDBATools.utils import dictfetchall
import datetime
#from inventory.forms import ServerAddForm
from mssql.forms import ServerAddForm
from django.core.mail import send_mail
# https://docs.djangoproject.com/en/2.1/topics/pagination/
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    categories = {'databaseinventory': databaseinventory,
                  'servermaintenance': servermaintenance}
    return render(request, 'mssql/index.html', context=categories)


def server(request):
    cursor = connection.cursor()
    try:
        cursor.execute("select * from dbo.Server")
        # https://stackoverflow.com/a/14294314/4449743
        serverData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    servers = {'serverData': serverData}
    return render(request, 'mssql/server.html', context=servers)


def server2(request):
    cursor = connection.cursor()
    try:
        cursor.execute("select * from dbo.Server")
        # https://stackoverflow.com/a/14294314/4449743
        serverData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    servers = {'serverData': serverData}
    return render(request, 'mssql/server2.html', context=servers)


def serveradd(request):
    form = ServerAddForm()

    if request.method == 'POST':
        form = ServerAddForm(request.POST)

        if form.is_valid():
            # Do Something
            form.save()

            srvName = form.cleaned_data['server']
            mailMsg = """Server ["""+srvName+"""] has been added in SQLDBATools inventory. 
Thanks & Regards
SQLDBATools
            """
            send_mail('Add Server - '+srvName,
                      mailMsg,
                      'ajay.dwivedi@tivo.com',
                      ['ajay.dwivedi@tivo.com'],
                      fail_silently=False,
                      )
        else:
            redirect('cfman:ServerAdd')

    return render(request, 'mssql/serveradd.html', context={'form': form})
