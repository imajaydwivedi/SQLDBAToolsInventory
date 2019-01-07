$srv = 'tul1dbapmtdb1\sql2016'
$db = 'TivoSQLInventory_Ajay'
$table = 'Instance'

$queryTableHeaders = @"
    select '<th>'+c.COLUMN_NAME+'</th>' from INFORMATION_SCHEMA.COLUMNS as c
	where c.TABLE_NAME = '$table'
"@;

# Get table Columns as Html Table Headers
$th = Invoke-Sqlcmd2 -SqlInstance $srv -Database $db -Query $queryTableHeaders
$th | Out-File c:\temp\th.txt
notepad c:\temp\th.txt


$queryTableRows = @"
    select '<td>{{ rec.'+lower(c.COLUMN_NAME)+' }}</td>' from INFORMATION_SCHEMA.COLUMNS as c
	where c.TABLE_NAME = '$table'
"@;

# Get table Columns as Html Table Headers
$td = Invoke-Sqlcmd2 -SqlInstance $srv -Database $db -Query $queryTableRows
$td | Out-File c:\temp\td.txt
notepad c:\temp\td.txt