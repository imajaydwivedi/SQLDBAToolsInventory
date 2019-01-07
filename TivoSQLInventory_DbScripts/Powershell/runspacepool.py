import json
from subprocess import Popen, PIPE
from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan
from SQLDBAToolsInventory_EnvironmentSettings import powershellbaseservername, proxyusername, proxypassword

# creates a https connection with explicit kerberos auth and implicit credentials
wsman = WSMan(powershellbaseservername, auth="kerberos", cert_validation=False)

pool = RunspacePool(wsman)
ps = PowerShell(pool)

script = '''
$psversiontable
'''
ps.add_command(script)
ps.invoke(["string", 1])
print(ps.output)
print(ps.streams.debug)


import json
from subprocess import Popen, PIPE
#servername = "tul1dbapmtdb1"
servername = "tul1cipedb2"
ps_cmdlet = """
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process -Force;
Import-Module SQLDBATools -DisableNameChecking;
$global:PrintUserFriendlyMessage = $false;
Get-ServerInfo {0} | ConvertTo-Json | Write-Output;
""".format(servername)
process = Popen(["powershell", ps_cmdlet], shell=True, stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()[0]
serverInfo_dict = json.loads(stdout)
print(serverInfo_dict['ServerName'])
