# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Databasebackup(models.Model):
    instanceid = models.ForeignKey('Instance', models.DO_NOTHING, db_column='InstanceID')  # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', max_length=125)  # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=128)  # Field name made lowercase.
    databasecreationdate = models.DateTimeField(db_column='DatabaseCreationDate')  # Field name made lowercase.
    recoverymodel = models.CharField(db_column='RecoveryModel', max_length=15)  # Field name made lowercase.
    lastfullbackupdate = models.DateTimeField(db_column='LastFullBackupDate', blank=True, null=True)  # Field name made lowercase.
    lastdifferentialbackupdate = models.DateTimeField(db_column='LastDifferentialBackupDate', blank=True, null=True)  # Field name made lowercase.
    lastlogbackupdate = models.DateTimeField(db_column='LastLogBackupDate', blank=True, null=True)  # Field name made lowercase.
    collectiontime = models.DateTimeField(db_column='CollectionTime', primary_key=True)  # Field name made lowercase.
    batchnumber = models.BigIntegerField(db_column='BatchNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DatabaseBackup'
        unique_together = (('collectiontime', 'instancename', 'databasename'),)


class Databases(models.Model):
    databaseid = models.AutoField(db_column='DatabaseID', primary_key=True)  # Field name made lowercase.
    instanceid = models.IntegerField(db_column='InstanceID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    datechecked = models.DateTimeField(db_column='DateChecked', blank=True, null=True)  # Field name made lowercase.
    autoclose = models.BooleanField(db_column='AutoClose', blank=True, null=True)  # Field name made lowercase.
    autocreatestatisticsenabled = models.BooleanField(db_column='AutoCreateStatisticsEnabled', blank=True, null=True)  # Field name made lowercase.
    autoshrink = models.BooleanField(db_column='AutoShrink', blank=True, null=True)  # Field name made lowercase.
    autoupdatestatisticsenabled = models.BooleanField(db_column='AutoUpdateStatisticsEnabled', blank=True, null=True)  # Field name made lowercase.
    availabilitydatabasesynchronizationstate = models.CharField(db_column='AvailabilityDatabaseSynchronizationState', max_length=16, blank=True, null=True)  # Field name made lowercase.
    availabilitygroupname = models.CharField(db_column='AvailabilityGroupName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    casesensitive = models.BooleanField(db_column='CaseSensitive', blank=True, null=True)  # Field name made lowercase.
    collation = models.CharField(db_column='Collation', max_length=40, blank=True, null=True)  # Field name made lowercase.
    compatibilitylevel = models.CharField(db_column='CompatibilityLevel', max_length=15, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    dataspaceusagekb = models.FloatField(db_column='DataSpaceUsageKB', blank=True, null=True)  # Field name made lowercase.
    encryptionenabled = models.BooleanField(db_column='EncryptionEnabled', blank=True, null=True)  # Field name made lowercase.
    indexspaceusagekb = models.FloatField(db_column='IndexSpaceUsageKB', blank=True, null=True)  # Field name made lowercase.
    isaccessible = models.BooleanField(db_column='IsAccessible', blank=True, null=True)  # Field name made lowercase.
    isfulltextenabled = models.BooleanField(db_column='IsFullTextEnabled', blank=True, null=True)  # Field name made lowercase.
    ismirroringenabled = models.BooleanField(db_column='IsMirroringEnabled', blank=True, null=True)  # Field name made lowercase.
    isparameterizationforced = models.BooleanField(db_column='IsParameterizationForced', blank=True, null=True)  # Field name made lowercase.
    isreadcommittedsnapshoton = models.BooleanField(db_column='IsReadCommittedSnapshotOn', blank=True, null=True)  # Field name made lowercase.
    issystemobject = models.BooleanField(db_column='IsSystemObject', blank=True, null=True)  # Field name made lowercase.
    isupdateable = models.BooleanField(db_column='IsUpdateable', blank=True, null=True)  # Field name made lowercase.
    lastbackupdate = models.DateTimeField(db_column='LastBackupDate', blank=True, null=True)  # Field name made lowercase.
    lastdifferentialbackupdate = models.DateTimeField(db_column='LastDifferentialBackupDate', blank=True, null=True)  # Field name made lowercase.
    lastlogbackupdate = models.DateTimeField(db_column='LastLogBackupDate', blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pageverify = models.CharField(db_column='PageVerify', max_length=17, blank=True, null=True)  # Field name made lowercase.
    readonly = models.BooleanField(db_column='ReadOnly', blank=True, null=True)  # Field name made lowercase.
    recoverymodel = models.CharField(db_column='RecoveryModel', max_length=10, blank=True, null=True)  # Field name made lowercase.
    replicationoptions = models.CharField(db_column='ReplicationOptions', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sizemb = models.FloatField(db_column='SizeMB', blank=True, null=True)  # Field name made lowercase.
    snapshotisolationstate = models.CharField(db_column='SnapshotIsolationState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    spaceavailablekb = models.FloatField(db_column='SpaceAvailableKB', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=35, blank=True, null=True)  # Field name made lowercase.
    targetrecoverytime = models.IntegerField(db_column='TargetRecoveryTime', blank=True, null=True)  # Field name made lowercase.
    inactive = models.BooleanField(db_column='InActive', blank=True, null=True)  # Field name made lowercase.
    lastread = models.DateTimeField(db_column='LastRead', blank=True, null=True)  # Field name made lowercase.
    lastwrite = models.DateTimeField(db_column='LastWrite', blank=True, null=True)  # Field name made lowercase.
    lastreboot = models.DateTimeField(db_column='LastReboot', blank=True, null=True)  # Field name made lowercase.
    lastdbccdate = models.DateTimeField(db_column='LastDBCCDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Databases'


class Datedimension(models.Model):
    datekey = models.IntegerField(db_column='DateKey', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    day = models.SmallIntegerField(db_column='Day')  # Field name made lowercase.
    daysuffix = models.CharField(db_column='DaySuffix', max_length=2)  # Field name made lowercase.
    weekday = models.SmallIntegerField(db_column='Weekday')  # Field name made lowercase.
    weekdayname = models.CharField(db_column='WeekDayName', max_length=10)  # Field name made lowercase.
    isweekend = models.BooleanField(db_column='IsWeekend')  # Field name made lowercase.
    isholiday = models.BooleanField(db_column='IsHoliday')  # Field name made lowercase.
    holidaytext = models.CharField(db_column='HolidayText', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dowinmonth = models.SmallIntegerField(db_column='DOWInMonth')  # Field name made lowercase.
    dayofyear = models.SmallIntegerField(db_column='DayOfYear')  # Field name made lowercase.
    weekofmonth = models.SmallIntegerField(db_column='WeekOfMonth')  # Field name made lowercase.
    weekofyear = models.SmallIntegerField(db_column='WeekOfYear')  # Field name made lowercase.
    isoweekofyear = models.SmallIntegerField(db_column='ISOWeekOfYear')  # Field name made lowercase.
    month = models.SmallIntegerField(db_column='Month')  # Field name made lowercase.
    monthname = models.CharField(db_column='MonthName', max_length=10)  # Field name made lowercase.
    quarter = models.SmallIntegerField(db_column='Quarter')  # Field name made lowercase.
    quartername = models.CharField(db_column='QuarterName', max_length=6)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    mmyyyy = models.CharField(db_column='MMYYYY', max_length=6)  # Field name made lowercase.
    monthyear = models.CharField(db_column='MonthYear', max_length=7)  # Field name made lowercase.
    firstdayofmonth = models.DateField(db_column='FirstDayOfMonth')  # Field name made lowercase.
    lastdayofmonth = models.DateField(db_column='LastDayOfMonth')  # Field name made lowercase.
    firstdayofquarter = models.DateField(db_column='FirstDayOfQuarter')  # Field name made lowercase.
    lastdayofquarter = models.DateField(db_column='LastDayOfQuarter')  # Field name made lowercase.
    firstdayofyear = models.DateField(db_column='FirstDayOfYear')  # Field name made lowercase.
    lastdayofyear = models.DateField(db_column='LastDayOfYear')  # Field name made lowercase.
    firstdayofnextmonth = models.DateField(db_column='FirstDayOfNextMonth')  # Field name made lowercase.
    firstdayofnextyear = models.DateField(db_column='FirstDayOfNextYear')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DateDimension'


class Excelsheetservers(models.Model):
    instance_id = models.BigAutoField(db_column='Instance_ID', primary_key=True)  # Field name made lowercase.
    sno = models.FloatField(db_column='SNo', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isvm = models.BooleanField(db_column='IsVM', blank=True, null=True)  # Field name made lowercase.
    nodetype = models.CharField(db_column='NodeType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    generaldescription = models.CharField(db_column='GeneralDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    environmenttype = models.CharField(db_column='EnvironmentType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businessunit = models.CharField(db_column='BusinessUnit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supportedapplication_field = models.CharField(db_column='SupportedApplication ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    domain = models.CharField(db_column='Domain', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    release = models.CharField(db_column='Release', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productkey = models.CharField(db_column='ProductKey', max_length=255, blank=True, null=True)  # Field name made lowercase.
    osversion = models.CharField(db_column='OSVersion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businessowner = models.CharField(db_column='BusinessOwner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primarycontact = models.CharField(db_column='PrimaryContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secondarycontact = models.CharField(db_column='SecondaryContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isdecommissioned = models.BooleanField(db_column='IsDecommissioned', blank=True, null=True)  # Field name made lowercase.
    ispowershelllinked = models.BooleanField(db_column='IsPowerShellLinked', blank=True, null=True)  # Field name made lowercase.
    issqlclusternode = models.BooleanField(db_column='IsSQLClusterNode', blank=True, null=True)  # Field name made lowercase.
    isalwaysonnode = models.BooleanField(db_column='IsAlwaysOnNode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExcelSheetServers'


class Instance(models.Model):
    instanceid = models.AutoField(db_column='InstanceID', primary_key=True)  # Field name made lowercase.
    serverid = models.ForeignKey('Server', models.DO_NOTHING, db_column='ServerID')  # Field name made lowercase.
    fqdn = models.ForeignKey('Server', models.DO_NOTHING, db_column='FQDN', blank=True, null=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=125, blank=True, null=True)  # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', unique=True, max_length=125, blank=True, null=True)  # Field name made lowercase.
    installdatadirectory = models.CharField(db_column='InstallDataDirectory', max_length=500, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='Edition', max_length=50)  # Field name made lowercase.
    productkey = models.CharField(db_column='ProductKey', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isclustered = models.BooleanField(db_column='IsClustered', blank=True, null=True)  # Field name made lowercase.
    iscasesensitive = models.BooleanField(db_column='IsCaseSensitive', blank=True, null=True)  # Field name made lowercase.
    ishadrenabled = models.BooleanField(db_column='IsHadrEnabled', blank=True, null=True)  # Field name made lowercase.
    isdecommissioned = models.BooleanField(db_column='IsDecommissioned', blank=True, null=True)  # Field name made lowercase.
    ispowershelllinked = models.BooleanField(db_column='IsPowerShellLinked', blank=True, null=True)  # Field name made lowercase.
    collectiontime = models.DateTimeField(db_column='CollectionTime')  # Field name made lowercase.
    commonversion = models.CharField(db_column='CommonVersion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    build = models.CharField(db_column='Build', max_length=4, blank=True, null=True)  # Field name made lowercase.
    versionstring = models.CharField(db_column='VersionString', max_length=18, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Instance'


class Server(models.Model):
    serverid = models.AutoField(db_column='ServerID', primary_key=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=125, blank=True, null=True)  # Field name made lowercase.
    environmenttype = models.CharField(db_column='EnvironmentType', max_length=125)  # Field name made lowercase.
    dnshostname = models.CharField(db_column='DNSHostName', max_length=125, blank=True, null=True)  # Field name made lowercase.
    fqdn = models.CharField(db_column='FQDN', unique=True, max_length=125, blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPAddress', max_length=15, blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=125, blank=True, null=True)  # Field name made lowercase.
    operatingsystem = models.CharField(db_column='OperatingSystem', max_length=125, blank=True, null=True)  # Field name made lowercase.
    spversion = models.CharField(db_column='SPVersion', max_length=125, blank=True, null=True)  # Field name made lowercase.
    isvm = models.BooleanField(db_column='IsVM', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=125, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=125, blank=True, null=True)  # Field name made lowercase.
    ram = models.IntegerField(db_column='RAM', blank=True, null=True)  # Field name made lowercase.
    cpu = models.SmallIntegerField(db_column='CPU', blank=True, null=True)  # Field name made lowercase.
    collectiontime = models.DateTimeField(db_column='CollectionTime', blank=True, null=True)  # Field name made lowercase.
    generaldescription = models.CharField(db_column='GeneralDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    powerplan = models.CharField(db_column='PowerPlan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osarchitecture = models.CharField(db_column='OSArchitecture', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Server'


class Unauthorizedserverrolemembers(models.Model):
    principal_name = models.CharField(max_length=128)
    type_desc = models.CharField(max_length=60, blank=True, null=True)
    role_permission = models.CharField(max_length=128, blank=True, null=True)
    roleorpermission = models.CharField(db_column='roleOrPermission', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'UnauthorizedServerRoleMembers'


class Volumeinfo(models.Model):
    id = models.BigAutoField(db_column='ID')  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', primary_key=True, max_length=125)  # Field name made lowercase.
    volumename = models.CharField(db_column='VolumeName', max_length=125)  # Field name made lowercase.
    capacitygb = models.DecimalField(db_column='CapacityGB', max_digits=20, decimal_places=2)  # Field name made lowercase.
    usedspacegb = models.DecimalField(db_column='UsedSpaceGB', max_digits=20, decimal_places=2)  # Field name made lowercase.
    usedspacepercent = models.DecimalField(db_column='UsedSpacePercent', max_digits=20, decimal_places=2)  # Field name made lowercase.
    freespacegb = models.DecimalField(db_column='FreeSpaceGB', max_digits=20, decimal_places=2)  # Field name made lowercase.
    label = models.CharField(db_column='Label', max_length=125, blank=True, null=True)  # Field name made lowercase.
    collectiontime = models.DateTimeField(db_column='CollectionTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VolumeInfo'
        unique_together = (('servername', 'volumename'),)


class VwGetappsyncdatabases(models.Model):
    currentserver = models.CharField(db_column='CurrentServer', max_length=128, blank=True, null=True)  # Field name made lowercase.
    subscribed_db = models.CharField(db_column='Subscribed_Db', max_length=37, blank=True, null=True)  # Field name made lowercase.
    target_db = models.CharField(db_column='Target_Db', max_length=37, blank=True, null=True)  # Field name made lowercase.
    tul1cipxidb2 = models.IntegerField(db_column='TUL1CIPXIDB2', blank=True, null=True)  # Field name made lowercase.
    tul1cspeldb02 = models.IntegerField(db_column='TUL1CSPELDB02', blank=True, null=True)  # Field name made lowercase.
    tul1cipcwrdb1 = models.IntegerField(db_column='TUL1CIPCWRDB1', blank=True, null=True)  # Field name made lowercase.
    tul1cipxdb12 = models.IntegerField(db_column='TUL1CIPXDB12', blank=True, null=True)  # Field name made lowercase.
    tul1cipxdb14 = models.IntegerField(db_column='TUL1CIPXDB14', blank=True, null=True)  # Field name made lowercase.
    tul1cipxdb15 = models.IntegerField(db_column='TUL1CIPXDB15', blank=True, null=True)  # Field name made lowercase.
    tul1cipxdb16 = models.IntegerField(db_column='TUL1CIPXDB16', blank=True, null=True)  # Field name made lowercase.
    tul1cipxdb17 = models.IntegerField(db_column='TUL1CIPXDB17', blank=True, null=True)  # Field name made lowercase.
    tul1cipxdb18 = models.IntegerField(db_column='TUL1CIPXDB18', blank=True, null=True)  # Field name made lowercase.
    tul1cipxdb20 = models.IntegerField(db_column='TUL1CIPXDB20', blank=True, null=True)  # Field name made lowercase.
    tul1cipxdb98 = models.IntegerField(db_column='TUL1CIPXDB98', blank=True, null=True)  # Field name made lowercase.
    tul1cipxdb99 = models.IntegerField(db_column='TUL1CIPXDB99', blank=True, null=True)  # Field name made lowercase.
    hasissue = models.CharField(db_column='HasIssue', max_length=3)  # Field name made lowercase.
    isrenamecase = models.CharField(db_column='IsRenameCase', max_length=3)  # Field name made lowercase.
    hasissue_tobeadded = models.CharField(db_column='HasIssue_ToBeAdded', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'Vw_GetAppSyncDatabases'


class VwDatabasebackups(models.Model):
    serverinstance = models.CharField(db_column='ServerInstance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=128)  # Field name made lowercase.
    databasecreationdate = models.DateTimeField(db_column='DatabaseCreationDate')  # Field name made lowercase.
    recoverymodel = models.CharField(db_column='RecoveryModel', max_length=15)  # Field name made lowercase.
    isfullbackupinlast24hours = models.CharField(db_column='IsFullBackupInLast24Hours', max_length=3)  # Field name made lowercase.
    isfullbackupinlast7days = models.CharField(db_column='IsFullBackupInLast7Days', max_length=3)  # Field name made lowercase.
    lastfullbackupdate = models.DateTimeField(db_column='LastFullBackupDate', blank=True, null=True)  # Field name made lowercase.
    lastdifferentialbackupdate = models.DateTimeField(db_column='LastDifferentialBackupDate', blank=True, null=True)  # Field name made lowercase.
    lastlogbackupdate = models.DateTimeField(db_column='LastLogBackupDate', blank=True, null=True)  # Field name made lowercase.
    collectiontime = models.DateTimeField(db_column='CollectionTime')  # Field name made lowercase.
    serverinstance_0 = models.CharField(db_column='ServerInstance', max_length=125)  # Field name made lowercase. Field renamed because of name conflict.
    databasename_0 = models.CharField(db_column='DatabaseName', max_length=128)  # Field name made lowercase. Field renamed because of name conflict.
    databasecreationdate_0 = models.DateTimeField(db_column='DatabaseCreationDate')  # Field name made lowercase. Field renamed because of name conflict.
    recoverymodel_0 = models.CharField(db_column='RecoveryModel', max_length=15)  # Field name made lowercase. Field renamed because of name conflict.
    isfullbackupinlast24hours_0 = models.CharField(db_column='IsFullBackupInLast24Hours', max_length=3)  # Field name made lowercase. Field renamed because of name conflict.
    isfullbackupinlast7days_0 = models.CharField(db_column='IsFullBackupInLast7Days', max_length=3)  # Field name made lowercase. Field renamed because of name conflict.
    lastfullbackupdate_0 = models.DateTimeField(db_column='LastFullBackupDate', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    lastdifferentialbackupdate_0 = models.DateTimeField(db_column='LastDifferentialBackupDate', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    lastlogbackupdate_0 = models.DateTimeField(db_column='LastLogBackupDate', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict.
    collectiontime_0 = models.DateTimeField(db_column='CollectionTime')  # Field name made lowercase. Field renamed because of name conflict.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vw_DatabaseBackups'
