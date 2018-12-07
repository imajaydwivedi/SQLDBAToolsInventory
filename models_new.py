# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Backuphistory(models.Model):
    backuphistid = models.AutoField(db_column='BackupHistId', primary_key=True)  # Field name made lowercase.
    instanceid = models.ForeignKey('Instance', models.DO_NOTHING, db_column='InstanceId')  # Field name made lowercase.
    databaseid = models.ForeignKey('Databases', models.DO_NOTHING, db_column='DatabaseId')  # Field name made lowercase.
    fullbackupdate = models.DateTimeField(db_column='FullbackupDate', blank=True, null=True)  # Field name made lowercase.
    diffbackupdate = models.DateTimeField(db_column='DiffBackupDate', blank=True, null=True)  # Field name made lowercase.
    tranbackupdate = models.DateTimeField(db_column='TranBackupDate', blank=True, null=True)  # Field name made lowercase.
    fullbackupsize = models.BigIntegerField(db_column='FullBackupSize', blank=True, null=True)  # Field name made lowercase.
    diffbackupsize = models.IntegerField(db_column='DiffBackupSize', blank=True, null=True)  # Field name made lowercase.
    tranbackupsize = models.IntegerField(db_column='TranBackupSize', blank=True, null=True)  # Field name made lowercase.
    fullbackupduration = models.IntegerField(db_column='FullBackupDuration', blank=True, null=True)  # Field name made lowercase.
    diffbackupduration = models.IntegerField(db_column='DiffBackupDuration', blank=True, null=True)  # Field name made lowercase.
    tranbackupduration = models.IntegerField(db_column='TranBackupDuration', blank=True, null=True)  # Field name made lowercase.
    compressed = models.BooleanField(db_column='Compressed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BackupHistory'


class Backupschedule(models.Model):
    bkuschedid = models.AutoField(db_column='BkuSchedId', primary_key=True)  # Field name made lowercase.
    instanceid = models.ForeignKey('Instance', models.DO_NOTHING, db_column='InstanceId')  # Field name made lowercase.
    databaseid = models.ForeignKey('Databases', models.DO_NOTHING, db_column='DatabaseId')  # Field name made lowercase.
    timefrom = models.DateTimeField(db_column='TimeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.DateTimeField(db_column='TimeTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BackupSchedule'


class Databases(models.Model):
    databaseid = models.AutoField(db_column='DatabaseId', primary_key=True)  # Field name made lowercase.
    instanceid = models.ForeignKey('Instance', models.DO_NOTHING, db_column='InstanceId')  # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=50)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    recoverymodel = models.CharField(db_column='RecoveryModel', max_length=64, blank=True, null=True)  # Field name made lowercase.
    currentdbsize = models.CharField(db_column='CurrentDBSize', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Databases'


class Instance(models.Model):
    instanceid = models.AutoField(db_column='InstanceID', primary_key=True)  # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', max_length=128)  # Field name made lowercase.
    serverid = models.ForeignKey('Server', models.DO_NOTHING, db_column='ServerID')  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sqlserviceaccountid = models.IntegerField(db_column='SQLServiceAccountID', blank=True, null=True)  # Field name made lowercase.
    authenticationmode = models.BooleanField(db_column='AuthenticationMode', blank=True, null=True)  # Field name made lowercase.
    saaccountname = models.CharField(db_column='saAccountName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    saaccountpassword = models.CharField(db_column='saAccountPassword', max_length=64, blank=True, null=True)  # Field name made lowercase.
    instanceclassification = models.SmallIntegerField(db_column='InstanceClassification', blank=True, null=True)  # Field name made lowercase.
    instancecores = models.SmallIntegerField(db_column='InstanceCores', blank=True, null=True)  # Field name made lowercase.
    instanceram = models.BigIntegerField(db_column='InstanceRAM', blank=True, null=True)  # Field name made lowercase.
    sqlserveragentaccountid = models.IntegerField(db_column='SQLServerAgentAccountID', blank=True, null=True)  # Field name made lowercase.
    defaultbkupath = models.CharField(db_column='DefaultBkuPath', max_length=250, blank=True, null=True)  # Field name made lowercase.
    defaultbkupathsize = models.CharField(db_column='DefaultBkuPathSize', max_length=20, blank=True, null=True)  # Field name made lowercase.
    defaultbkupathfree = models.CharField(db_column='DefaultBkuPathFree', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Instance'


class Server(models.Model):
    serverid = models.IntegerField(db_column='ServerID', primary_key=True)  # Field name made lowercase.
    server = models.CharField(db_column='Server', max_length=128, blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=25, blank=True, null=True)  # Field name made lowercase.
    servertype = models.CharField(db_column='ServerType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='ShortDescription', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sqlstate = models.CharField(db_column='SQLState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  # Field name made lowercase.
    businessunit = models.CharField(db_column='BusinessUnit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    sqlversion = models.CharField(db_column='SQLVersion', max_length=64, blank=True, null=True)  # Field name made lowercase.
    sockets = models.IntegerField(db_column='Sockets', blank=True, null=True)  # Field name made lowercase.
    cores = models.IntegerField(db_column='Cores', blank=True, null=True)  # Field name made lowercase.
    logicalprocs = models.IntegerField(db_column='LogicalProcs', blank=True, null=True)  # Field name made lowercase.
    businessowner = models.CharField(db_column='Businessowner', max_length=25, blank=True, null=True)  # Field name made lowercase.
    technicalowner = models.CharField(db_column='TechnicalOwner', max_length=25, blank=True, null=True)  # Field name made lowercase.
    secondarytechnicalowner = models.CharField(db_column='SecondaryTechnicalOwner', max_length=25, blank=True, null=True)  # Field name made lowercase.
    additionalnotes = models.TextField(db_column='AdditionalNotes', blank=True, null=True)  # Field name made lowercase.
    backuppsdeployed = models.BooleanField(db_column='BackupPSDeployed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Server'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
