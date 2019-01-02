from django.db import models


class Server(models.Model):
    # Field name made lowercase.
    serverid = models.AutoField(db_column='ServerID', primary_key=True)
    # Field name made lowercase.
    server = models.CharField(
        db_column='Server', max_length=128, blank=True, null=True)
    # Field name made lowercase.
    DOMAIN_CHOICES = (
        ('Corporate', 'Corporate'),
        ('Armus', 'Armus'),
        ('Angoss', 'Angoss'),
        ('NA', 'Not Available'),
    )
    domain = models.CharField(
        db_column='Domain', max_length=25, blank=True, null=True, choices=DOMAIN_CHOICES, default='Corporate')
    # Field name made lowercase.
    SERVERTYPE_CHOICES = (
        ('NA', 'Not Available'),
        ('Cluster Instance', 'Cluster Instance'),
        ('Decommissioned/To Be Decommissioned',
         'Decommissioned/To Be Decommissioned'),
        ('Dev', 'Development'),
        ('DR', 'Disaster Recovery'),
        ('DTC Cluster Instance', 'DTC Cluster Instance'),
        ('Prod', 'Production'),
        ('Win Cluster', 'Windows Cluster'),
    )
    servertype = models.CharField(
        db_column='ServerType', max_length=50, blank=True, null=True, choices=SERVERTYPE_CHOICES, default='Prod')
    # Field name made lowercase.
    shortdescription = models.CharField(
        db_column='ShortDescription', max_length=128, blank=True, null=True)
    # Field name made lowercase.
    SQLSTATE_CHOICES = (
        ('Start', 'Started'),
        ('Stop', 'Stopped'),
        ('Pause', 'Paused'),
    )
    sqlstate = models.CharField(
        db_column='SQLState', max_length=20, blank=True, null=True, choices=SQLSTATE_CHOICES, default='Start')
    # Field name made lowercase.
    CATEGORY_CHOICES = (
        ('NA', 'Not Available'),
        ('Corporate', 'Corporate'),
        ('IT', 'IT'),
        ('Product', 'Product'),
    )
    category = models.CharField(
        db_column='Category', max_length=20, blank=True, null=True, choices=CATEGORY_CHOICES, default='Product')
    # Field name made lowercase.
    BUSINESSUNIT_CHOICES = (
        ('NA', 'Not Available'),
        ('Advertising', 'Advertising'),
        ('Finance', 'Finance'),
        ('IPG', 'IPG'),
        ('IT', 'IT'),
        ('MetaData', 'MetaData'),
        ('Sales', 'Sales'),
    )
    businessunit = models.CharField(
        db_column='BusinessUnit', max_length=20, blank=True, null=True, choices=BUSINESSUNIT_CHOICES, default='MetaData')
    # Field name made lowercase.
    OS_CHOICES = (
        ('NA', 'Not Available'),
        ('Microsoft Windows 2000 Server', 'Microsoft Windows 2000 Server'),
        ('Microsoft Windows Server 2008  Enterprise',
         'Microsoft Windows Server 2008  Enterprise'),
        ('Microsoft Windows Server 2008 R2 Enterprise',
         'Microsoft Windows Server 2008 R2 Enterprise'),
        ('Microsoft Windows Server 2008 R2 Standard',
         'Microsoft Windows Server 2008 R2 Standard'),
        ('Microsoft Windows Server 2012 R2 Datacenter',
         'Microsoft Windows Server 2012 R2 Datacenter'),
        ('Microsoft Windows Server 2012 R2 Standard',
         'Microsoft Windows Server 2012 R2 Standard'),
        ('Microsoft Windows Server 2012 Standard',
         'Microsoft Windows Server 2012 Standard'),
        ('Microsoft Windows Server 2016 Standard',
         'Microsoft Windows Server 2016 Standard'),
        ('Microsoft(R) Windows(R) Server 2003 Enterprise x64 Edition',
         'Microsoft(R) Windows(R) Server 2003 Enterprise x64 Edition'),
        ('Microsoft(R) Windows(R) Server 2003 Standard x64 Edition',
         'Microsoft(R) Windows(R) Server 2003 Standard x64 Edition'),
        ('Microsoft(R) Windows(R) Server 2003~ Enterprise Edition',
         'Microsoft(R) Windows(R) Server 2003~ Enterprise Edition'),
        ('Microsoft(R) Windows(R) Server 2003~ Standard Edition',
         'Microsoft(R) Windows(R) Server 2003~ Standard Edition'),
        ('Microsoft® Windows Server® 2008 Enterprise',
         'Microsoft® Windows Server® 2008 Enterprise'),
        ('Microsoft® Windows Server® 2008 Standard',
         'Microsoft® Windows Server® 2008 Standard'),
    )
    os = models.CharField(db_column='OS', max_length=64, blank=True, null=True,
                          choices=OS_CHOICES, default='Microsoft Windows Server 2012 R2 Standard')
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
    # Field name made lowercase.
    SQLTYPE_CHOICES = (
        ('MSSQL', 'Sql Server'),
        ('Oracle', 'Oracle'),
        ('MySQL', 'MySQL'),
        ('Hadoop', 'Hadoop'),
        ('Mongo', 'Mongo'),
        ('SQLlite', 'SQLlite'),
        ('Other', 'Other')
    )
    sqltype = models.CharField(
        db_column='SQLType', max_length=20, blank=True, null=True, choices=SQLTYPE_CHOICES, default='MSSQL')

    class Meta:
        managed = False
        db_table = 'Server'

    def __str__(self):
        return "{}  ({})".format(self.server, self.serverid)


class Instance(models.Model):
    # Field name made lowercase.
    instanceid = models.AutoField(db_column='InstanceID', primary_key=True)
    # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', max_length=128)
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
    # Field name made lowercase.
    maxjobcount = models.IntegerField(
        db_column='maxJobCount', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Instance'

    def __str__(self):
        # return self.instancename
        return "{}  ({})".format(self.instancename, self.instanceid)


class Database(models.Model):
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
    RECOVERYMODEL_CHOICES = (
        ('Simple', 'Simple'),
        ('Bulk-Logged', 'Bulk-Logged'),
        ('Full', 'Full'),
    )
    recoverymodel = models.CharField(
        db_column='RecoveryModel', max_length=64, blank=True, null=True, choices=RECOVERYMODEL_CHOICES, default='Full')
    # Field name made lowercase.
    currentdbsize = models.CharField(
        db_column='CurrentDBSize', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    backuppath = models.CharField(
        db_column='BackupPath', max_length=128, blank=True, null=True)
    
    # Custom fields start here
    # sqlinstance = models.ForeignKey(
    #     'Instance', models.DO_NOTHING, db_column='InstanceName')

    class Meta:
        managed = False
        db_table = 'Databases'

    def __str__(self):
        # return self.databasename
        return "{}  ({})".format(self.databasename, self.databaseid)

    # def sqlInstance(self):
    #     return Instance.objects.filter(instanceid = self.instanceid)[0].instancename


class Backupschedule(models.Model):
    # Field name made lowercase.
    bkuschedid = models.AutoField(db_column='BkuSchedId', primary_key=True)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId')
    # Field name made lowercase.
    timefrom = models.TimeField(db_column='TimeFrom', blank=True, null=True)
    # Field name made lowercase.
    timeto = models.TimeField(db_column='TimeTo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BackupSchedule'

    def __str__(self):
        return self.bkuschedid + '  (' + str(self.timefrom) + ' - ' + str(self.timeto) + ')'


class Commandqueue(models.Model):
    # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=254)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId')
    # Field name made lowercase.
    databaseid = models.ForeignKey(
        'Database', models.DO_NOTHING, db_column='DatabaseId')
    # Field name made lowercase.
    command = models.TextField(db_column='Command')
    # Field name made lowercase.
    jobid = models.CharField(
        db_column='jobId', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    JOBTYPE_CHOICES = (
        ('BKU','BKU'),
        ('NA','Not Available'),
    )
    jobtype = models.CharField(db_column='JobType', max_length=20,choices = JOBTYPE_CHOICES, default='BKU')
    # Field name made lowercase.
    STATUS_CHOICES = (
        ('Scheduled','Scheduled'),
        ('NA','Not Available'),
    )
    status = models.CharField(db_column='Status', max_length=10, choices=STATUS_CHOICES, default = 'Scheduled')
    reason = models.TextField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'CommandQueue'


class Logging(models.Model):
    # Field name made lowercase.
    logid = models.AutoField(db_column='logId', primary_key=True)
    # Field name made lowercase.
    logmessage = models.TextField(db_column='LogMessage')

    class Meta:
        managed = False
        db_table = 'Logging'


# class Sqlsyntax(models.Model):
#     # Field name made lowercase.
#     syntaxid = models.AutoField(db_column='SyntaxID')
#     # Field name made lowercase.
#     sqlversion = models.CharField(db_column='SQLVersion', max_length=128)
#     # Field name made lowercase.
#     sqltype = models.CharField(db_column='SQLType', max_length=10)
#     # Field name made lowercase.
#     sqlsyntax = models.TextField(db_column='SQLSyntax')
#     # Field name made lowercase.
#     syntaxtype = models.CharField(
#         db_column='SyntaxType', max_length=10, blank=True, null=True)
#     # Field name made lowercase.
#     sqlparams = models.CharField(
#         db_column='SQLParams', max_length=128, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'SQLSyntax'


class Backuphistory(models.Model):
    # Field name made lowercase.
    backuphistid = models.AutoField(db_column='BackupHistId', primary_key=True)
    # Field name made lowercase.
    instanceid = models.ForeignKey(
        'Instance', models.DO_NOTHING, db_column='InstanceId')
    # Field name made lowercase.
    databaseid = models.ForeignKey(
        'Database', models.DO_NOTHING, db_column='DatabaseId')
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
    fullbackupsize = models.DecimalField(
        db_column='FullBackupSize', max_digits=20, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    diffbackupsize = models.DecimalField(
        db_column='DiffBackupSize', max_digits=20, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    tranbackupsize = models.DecimalField(
        db_column='TranBackupSize', max_digits=20, decimal_places=0, blank=True, null=True)
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
