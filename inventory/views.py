from django.shortcuts import render
from django.http import HttpResponse
import datetime
from inventory.models import *
  # https://docs.djangoproject.com/en/2.1/topics/pagination/
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    # https://docs.djangoproject.com/en/2.1/topics/db/sql/#mapping-query-fields-to-model-fields
    server_list = Server.objects.order_by('server')
    instance_list = Instance.objects.all()
    database_list = Database.objects.all()
    backuphistory_list = Backuphistory.objects.all()
    
    paginator = Paginator(server_list, 5)  # Show 5 servers per page
    page = request.GET.get('page', 1)
    servers = paginator.get_page(page)

    inventory_dict = {'server_records': servers,
                      # 'instance_records': instance_list,
                      # 'database_records': database_list,
                      # 'backuphistory_records': backuphistory_list
                      }
    return render(request, 'inventory/index.html', context=inventory_dict)


def test(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
