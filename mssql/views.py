from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import connection
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

#from inventory.forms import ServerAddForm
from mssql.forms import *
from SQLDBATools.utils import dictfetchall
# Server, Instance, Database, Backuphistory, Backuphistory, Commandqueue, Logging
from mssql.models import *

# packages for PowerShell call
from pypsrp.client import Client
import json
from SQLDBAToolsInventory_EnvironmentSettings import powershellbaseservername, proxyusername, proxypassword

# https://docs.djangoproject.com/en/2.1/topics/pagination/


@login_required
def index(request):
    categories = {'databaseinventory': databaseinventory,
                  'servermaintenance': servermaintenance}
    return render(request, 'mssql/index.html', context=categories)


@login_required
def server(request):
    cursor = connection.cursor()
    try:
        cursor.execute("select * from Server")
        # https://stackoverflow.com/a/14294314/4449743
        serverData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    servers = {'serverData': serverData}
    return render(request, 'mssql/server.html', context=servers)


def serverx(request):
    cursor = connection.cursor()
    try:
        cursor.execute("select * from Server")
        # https://stackoverflow.com/a/14294314/4449743
        serverData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    servers = {'serverData': serverData}
    return render(request, 'mssql/serverx.html', context=servers)


@login_required
def instance(request):
    cursor = connection.cursor()
    try:
        cursor.execute("""select i.[InstanceID]
      ,i.[InstanceName]
      ,s.[Server]
      ,i.[Port]
      ,i.[IPAddress]
      ,i.[SQLServiceAccountID]
      ,i.[AuthenticationMode]
      ,i.[saAccountName]
      ,i.[saAccountPassword]
      ,i.[InstanceClassification]
      ,i.[InstanceCores]
      ,i.[InstanceRAM]
      ,i.[SQLServerAgentAccountID]
      ,i.[DefaultBkuPath]
      ,i.[DefaultBkuPathSize]
      ,i.[DefaultBkuPathFree]
      ,i.[maxJobCount] 
from Instance as i join Server as s on s.ServerID = i.ServerID""")
        # https://stackoverflow.com/a/14294314/4449743
        instanceData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    instances = {'instanceData': instanceData}
    return render(request, 'mssql/instance.html', context=instances)


@login_required
def database(request):
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT d.[DatabaseId]
      ,i.InstanceName
      ,d.[DatabaseName]
      ,d.[CreatedDate]
      ,d.[RecoveryModel]
      ,d.[CurrentDBSize]
      ,d.[BackupPath]
  FROM [Databases] as d
  JOIN Instance as i
  ON i.InstanceID = d.InstanceId""")
        # https://stackoverflow.com/a/14294314/4449743
        databaseData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    databases = {'databaseData': databaseData}
    return render(request, 'mssql/database.html', context=databases)


def server2(request):
    cursor = connection.cursor()
    try:
        cursor.execute("select * from Server")
        # https://stackoverflow.com/a/14294314/4449743
        serverData = dictfetchall(cursor)
    # catch:
        #raise ValueError('Could not fetch data from INFORMATION_SCHEMA.COLUMNS')
    finally:
        cursor.close()

    servers = {'serverData': serverData}
    return render(request, 'mssql/server2.html', context=servers)


@login_required
def serveradd(request):
    form = None
    returnSuccessMessage = None
    returnErrorMessage = None

    if request.method == 'POST':
        srvName = request.POST.get('server')
        useremail = request.user.email
        srvObj = Server.objects.filter(server=srvName).first()

        if srvObj:
            returnSuccessMessage = "Server [{0}] has already been added in Inventory.".format(
                srvName)
        else:
            form = ServerAddForm(request.POST)

            if form.is_valid():
                form.save()

                mailMsg = """Server ["""+srvName+"""] has been added in SQLDBATools inventory. 


                
    Thanks & Regards
    SQLDBATools
                """
                send_mail('Add Server - '+srvName,
                          mailMsg,
                          'ajay.dwivedi@tivo.com',
                          [useremail],
                          fail_silently=False,
                          )

                returnSuccessMessage = "Server [{0}] has been successfully added in Inventory.".format(
                    srvName)
            else:
                returnErrorMessage = "Kindly verify the server details as it seems invalid."
                #form = ServerAddForm()
                redirect('cfman:ServerAdd')
    else:
        print("Return blank form to be filled by user!")
        form = ServerAddForm()

    server = {
        'form': form,
        'returnSuccessMessage': returnSuccessMessage,
        'returnErrorMessage': returnErrorMessage,
    }
    return render(request, 'mssql/serveradd.html', context=server)


# Function to used used for Discovering ServerInfo
@login_required
def serveradd_ps(request):
    getServerInfo = None
    addServerSubmitted = None
    serverInfoform = None

    if request.method == 'POST':
        servername = request.POST.get('ServerName')

        # put code if user wants ServerInfo
        if 'Get-ServerInfo' in request.POST:
            print("Get-ServerInfo powershell cmdlet called!")
            client = Client(powershellbaseservername,
                            username=proxyusername, password=proxypassword, ssl=False)

            #servername = 'tul1dbapmtdb1'
            #servername = request.POST.get('ServerName')
            script = r"""
            Import-Module SQLDBATools -DisableNameChecking;
            import-module dbatools;
            Get-ServerInfo '{0}' | ConvertTo-Json | Write-Output
            """.format(servername)

            output, streams, had_errors = client.execute_ps(script)

            if had_errors:
                print("Error occurred in powershell script execution")
                print("ERROR:\n%s" % "\n".join(
                    [str(s) for s in streams.error]))
            else:
                serverInfo_dict = json.loads(output)
                print(serverInfo_dict['LastBootTime'])
            getServerInfo = GetServerInfoForm(serverInfo_dict)

        # if user wants to submit Add-ServerInfo
        elif 'Add-ServerInfo' in request.POST:
            print("Add-ServerInfo form submitted!")
            addServerSubmitted = servername
    else:
        print("Add-ServerInfo form called!")
        serverInfoform = AddServerInfoForm()

    serverDetails = {'getServerInfo': getServerInfo,
                     'addServerSubmitted': addServerSubmitted,
                     'serverInfoform': serverInfoform,
                     }
    return render(request, 'mssql/serveradd_ps.html', context=serverDetails)


@login_required
def instanceadd(request):
    form = None
    returnSuccessMessage = None
    returnErrorMessage = None

    if request.method == 'POST':
        instanceName = request.POST.get('instancename')
        #print("InstanceName = {0}".format(instanceName))
        useremail = request.user.email
        instanceObj = Instance.objects.filter(
            instancename=instanceName).first()

        if instanceObj:
            returnSuccessMessage = "SqlInstance [{0}] has already been added in Inventory.".format(
                instanceName)
        else:
            form = InstanceAddForm(request.POST)

            if form.is_valid():
                form.save()

                mailMsg = """SqlInstance ["""+instanceName+"""] has been added in SQLDBATools inventory. 



    Thanks & Regards
    SQLDBATools
                """
                send_mail('Add SqlInstance - '+instanceName,
                          mailMsg,
                          'ajay.dwivedi@tivo.com',
                          [useremail],
                          fail_silently=False,
                          )

                returnSuccessMessage = "SqlInstance [{0}] has been successfully added in Inventory.".format(
                    instanceName)
            else:
                returnErrorMessage = "Kindly verify the SqlInstance details as it seems invalid."
                #form = ServerAddForm()
                redirect('cfman:InstanceAdd')
    else:
        print("Return blank form to be filled by user!")
        form = InstanceAddForm()

    instance = {
        'form': form,
        'returnSuccessMessage': returnSuccessMessage,
        'returnErrorMessage': returnErrorMessage,
    }
    return render(request, 'mssql/instanceadd.html', context=instance)


@login_required
def databaseadd(request):
    form = None
    returnSuccessMessage = None
    returnErrorMessage = None

    if request.method == 'POST':
        databaseName = request.POST.get('databasename')
        instanceId = request.POST.get('instanceid')
        #print("InstanceID = {0}".format(instanceId))
        #username = request.user.username
        useremail = request.user.email

        databaseObj = Database.objects.filter(
            databasename=databaseName, instanceid=instanceId).first()

        if databaseObj:
            returnSuccessMessage = "Database [{0}] has already been added in Inventory.".format(
                databaseName)
        else:
            form = DatabaseAddForm(request.POST)

            if form.is_valid():
                form.save()

                mailMsg = """Database ["""+databaseName+"""] has been added in SQLDBATools inventory. 



    Thanks & Regards
    SQLDBATools
                """
                send_mail('Add Database - '+databaseName,
                          mailMsg,
                          'ajay.dwivedi@tivo.com',
                          [useremail],
                          fail_silently=False,
                          )

                returnSuccessMessage = "Datbase [{0}] has been successfully added in Inventory.".format(
                    databaseName)
            else:
                returnErrorMessage = "Kindly verify the database details as it seems invalid."
                redirect('cfman:DatabaseAdd')
    else:
        print("Return blank form to be filled by user!")
        form = DatabaseAddForm()

    database = {
        'form': form,
        'returnSuccessMessage': returnSuccessMessage,
        'returnErrorMessage': returnErrorMessage,
    }
    return render(request, 'mssql/databaseadd.html', context=database)
