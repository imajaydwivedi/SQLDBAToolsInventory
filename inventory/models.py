from django.db import models

class Server(models.Model):
    # Field name made lowercase.
    serverid = models.IntegerField(db_column='ServerID', primary_key=True)
    # Field name made lowercase.
    server = models.CharField(
        db_column='Server', max_length=128, blank=True, null=True)
    # Field name made lowercase.
    domain = models.CharField(
        db_column='Domain', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    servertype = models.CharField(
        db_column='ServerType', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    shortdescription = models.CharField(
        db_column='ShortDescription', max_length=128, blank=True, null=True)
    # Field name made lowercase.
    sqlstate = models.CharField(
        db_column='SQLState', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    category = models.CharField(
        db_column='Category', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    businessunit = models.CharField(
        db_column='BusinessUnit', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    sqlversion = models.CharField(
        db_column='SQLVersion', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    sockets = models.IntegerField(db_column='Sockets', blank=True, null=True)
    # Field name made lowercase.
    cores = models.IntegerField(db_column='Cores', blank=True, null=True)
    # Field name made lowercase.
    logicalprocs = models.IntegerField(
        db_column='LogicalProcs', blank=True, null=True)
    # Field name made lowercase.
    businessowner = models.CharField(
        db_column='Businessowner', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    technicalowner = models.CharField(
        db_column='TechnicalOwner', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    secondarytechnicalowner = models.CharField(
        db_column='SecondaryTechnicalOwner', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    additionalnotes = models.TextField(
        db_column='AdditionalNotes', blank=True, null=True)
    # Field name made lowercase.
    backuppsdeployed = models.BooleanField(
        db_column='BackupPSDeployed', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Server'

    # def __str__(self):
    #     return "{}({})".format(self.server, self.serverid)

    # def server_name_id_link(self):
    #     return format_html('<a href="\"span style="color: #{};">{}</span>',
    #                        self.color_code,
    #                        self.first_name)

    # server_name_id_link.allow_tags = True
    # server_name_id_link.admin_order_field = 'first_name'


class Instance(models.Model):
    # Field name made lowercase.
    instanceid = models.AutoField(db_column='InstanceID', primary_key=True)
    # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', max_length=128)
    # servername = models.CharField("Server Name",max_length=128) # Computed Column
    # Field name made lowercase.
    serverid = models.ForeignKey(
        'Server', models.DO_NOTHING, db_column='ServerID')
    # Field name made lowercase.
    port = models.CharField(
        db_column='Port', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    ipaddress = models.CharField(
        db_column='IPAddress', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    sqlserviceaccountid = models.IntegerField(
        db_column='SQLServiceAccountID', blank=True, null=True)
    # Field name made lowercase.
    authenticationmode = models.BooleanField(
        db_column='AuthenticationMode', blank=True, null=True)
    # Field name made lowercase.
    saaccountname = models.CharField(
        db_column='saAccountName', max_length=128, blank=True, null=True)
    # Field name made lowercase.
    saaccountpassword = models.CharField(
        db_column='saAccountPassword', max_length=64, blank=True, null=True)
    instanceclassification = models.SmallIntegerField(
        db_column='InstanceClassification', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    instancecores = models.SmallIntegerField(
        db_column='InstanceCores', blank=True, null=True)
    # Field name made lowercase.
    instanceram = models.BigIntegerField(
        db_column='InstanceRAM', blank=True, null=True)
    # Field name made lowercase.
    sqlserveragentaccountid = models.IntegerField(
        db_column='SQLServerAgentAccountID', blank=True, null=True)
    # Field name made lowercase.
    defaultbkupath = models.CharField(
        db_column='DefaultBkuPath', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    defaultbkupathsize = models.CharField(
        db_column='DefaultBkuPathSize', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    defaultbkupathfree = models.CharField(
        db_column='DefaultBkuPathFree', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Instance'

    def __str__(self):
        return self.instancename


class Databases(models.Model):
    # Field name made lowercase.
    databaseid = models.AutoField(db_column='DatabaseId', primary_key=True)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId')
    # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=50)
    # Field name made lowercase.
    createddate = models.DateTimeField(
        db_column='CreatedDate', blank=True, null=True)
    # Field name made lowercase.
    recoverymodel = models.CharField(
        db_column='RecoveryModel', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    currentdbsize = models.CharField(
        db_column='CurrentDBSize', max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Databases'

    def __str__(self):
        return self.databasename


class Backupschedule(models.Model):
    # Field name made lowercase.
    bkuschedid = models.AutoField(db_column='BkuSchedId', primary_key=True)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId')
    # Field name made lowercase.
    databaseid = models.ForeignKey(
        'Databases', models.DO_NOTHING, db_column='DatabaseId')
    # Field name made lowercase.
    timefrom = models.DateTimeField(
        db_column='TimeFrom', blank=True, null=True)
    # Field name made lowercase.
    timeto = models.DateTimeField(db_column='TimeTo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BackupSchedule'

    def __str__(self):
        return self.bkuschedid + '(' + str(self.timefrom) + str(timeto) + ')'


class Backuphistory(models.Model):
    # Field name made lowercase.
    backuphistid = models.AutoField(db_column='BackupHistId', primary_key=True)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId')
    # Field name made lowercase.
    databaseid = models.ForeignKey(
        'Databases', models.DO_NOTHING, db_column='DatabaseId')
    # Field name made lowercase.
    fullbackupdate = models.DateTimeField(
        db_column='FullbackupDate', blank=True, null=True)
    # Field name made lowercase.
    diffbackupdate = models.DateTimeField(
        db_column='DiffBackupDate', blank=True, null=True)
    # Field name made lowercase.
    tranbackupdate = models.DateTimeField(
        db_column='TranBackupDate', blank=True, null=True)
    # Field name made lowercase.
    fullbackupsize = models.BigIntegerField(
        db_column='FullBackupSize', blank=True, null=True)
    # Field name made lowercase.
    diffbackupsize = models.IntegerField(
        db_column='DiffBackupSize', blank=True, null=True)
    # Field name made lowercase.
    tranbackupsize = models.IntegerField(
        db_column='TranBackupSize', blank=True, null=True)
    # Field name made lowercase.
    fullbackupduration = models.IntegerField(
        db_column='FullBackupDuration', blank=True, null=True)
    # Field name made lowercase.
    diffbackupduration = models.IntegerField(
        db_column='DiffBackupDuration', blank=True, null=True)
    # Field name made lowercase.
    tranbackupduration = models.IntegerField(
        db_column='TranBackupDuration', blank=True, null=True)
    # Field name made lowercase.
    compressed = models.BooleanField(
        db_column='Compressed', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BackupHistory'
