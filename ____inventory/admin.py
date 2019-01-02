from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import *
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['serverid', 'server', 'domain', 'servertype', 'businessunit',
                    'logicalprocs', 'businessowner', 'technicalowner', 'backuppsdeployed']
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site#Add_list_filters
    list_filter = ('backuppsdeployed', 'servertype', 'domain')

    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ['server', 'serverid']


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ['instanceid', 'instancename', 'server_link',
                    'instancecores', 'instanceram', 'defaultbkupath']

    # https://avilpage.com/2017/11/django-tips-tricks-hyperlink-foreignkey-admin.html
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    def server_link(self, instance):
        url = reverse("admin:inventory_server_change",
                      args=[instance.serverid.serverid])
        link = '<a href="%s">%s</a>' % (url, instance.serverid.server)
        return mark_safe(link)
    server_link.short_description = 'Server'

    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ['instanceid', 'instancename']


@admin.register(Database)
class DatabasesAdmin(admin.ModelAdmin):
    list_display = ['databaseid', 'instance_link', 'databasename',
                    'createddate', 'recoverymodel', 'currentdbsize']

    # https://avilpage.com/2017/11/django-tips-tricks-hyperlink-foreignkey-admin.html
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    def instance_link(self, database):
        url = reverse("admin:inventory_instance_change",
                      args=[database.instanceid.instanceid])
        link = '<a href="%s">%s</a>' % (url, database.instanceid.instancename)
        return mark_safe(link)
    instance_link.short_description = 'SqlInstance'

    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ["instanceid__instancename", 'databasename']

    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site#Add_list_filters
    list_filter = ['recoverymodel']


@admin.register(Backupschedule)
class BackupscheduleAdmin(admin.ModelAdmin):
    list_display = ['bkuschedid', 'instance_link',
                    'timefrom', 'timeto']

    # https://avilpage.com/2017/11/django-tips-tricks-hyperlink-foreignkey-admin.html
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    def instance_link(self, backupschedule):
        url = reverse("admin:inventory_instance_change",
                      args=[backupschedule.instanceid.instanceid])
        link = '<a href="%s">%s</a>' % (url,
                                        backupschedule.instanceid.instancename)
        return mark_safe(link)
    instance_link.short_description = 'SqlInstance'

    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ["instanceid__instancename"]

    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site#Add_list_filters
    list_filter = ['timefrom', 'timeto']


@admin.register(Backuphistory)
class BackuphistoryAdmin(admin.ModelAdmin):
    list_display = ['backuphistid', 'instance_link', 'database_link',
                    'fullbackupdate', 'diffbackupdate', 'tranbackupdate']

    # https://avilpage.com/2017/11/django-tips-tricks-hyperlink-foreignkey-admin.html
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    def instance_link(self, backuphistory):
        url = reverse("admin:inventory_instance_change",
                      args=[backuphistory.instanceid.instanceid])
        link = '<a href="%s">%s</a>' % (url,
                                        backuphistory.instanceid.instancename)
        return mark_safe(link)
    instance_link.short_description = 'SqlInstance'

    # https://avilpage.com/2017/11/django-tips-tricks-hyperlink-foreignkey-admin.html
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    def database_link(self, backuphistory):
        url = reverse("admin:inventory_database_change",
                      args=[backuphistory.databaseid.databaseid])
        link = '<a href="%s">%s</a>' % (url,
                                        backuphistory.databaseid.databasename)
        return mark_safe(link)
    database_link.short_description = 'Database'

    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ["instanceid__instancename", "databaseid__databasename"]


@admin.register(Commandqueue)
class CommandqueueAdmin(admin.ModelAdmin):
    list_display = ['id', 'instance_link', 'database_link',
                    'command', 'jobtype', 'status', 'reason', 'priority']

    # https://avilpage.com/2017/11/django-tips-tricks-hyperlink-foreignkey-admin.html
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    def instance_link(self, commandqueue):
        url = reverse("admin:inventory_instance_change",
                      args=[commandqueue.instanceid.instanceid])
        link = '<a href="%s">%s</a>' % (url,
                                        commandqueue.instanceid.instancename)
        return mark_safe(link)
    instance_link.short_description = 'SqlInstance'

    # https://avilpage.com/2017/11/django-tips-tricks-hyperlink-foreignkey-admin.html
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    def database_link(self, commandqueue):
        url = reverse("admin:inventory_database_change",
                      args=[commandqueue.databaseid.databaseid])
        link = '<a href="%s">%s</a>' % (url,
                                        commandqueue.databaseid.databasename)
        return mark_safe(link)
    database_link.short_description = 'Database'

    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ["instanceid__instancename", "databaseid__databasename"]

    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site#Add_list_filters
    list_filter = ['jobtype', 'status', 'priority']


@admin.register(Logging)
class LoggingAdmin(admin.ModelAdmin):
    list_display = ['logid', 'logmessage']

