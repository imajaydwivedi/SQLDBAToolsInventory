from SQLDBAToolsInventory_EnvironmentSettings import powershellbaseservername,proxyusername,proxypassword
from SQLDBATools.utils import dictfetchall
from pypsrp.client import Client
import json
# Create your tests here.



servername = "tul1cipedb2"

# put code if user wants ServerInfo
print("Get-ServerInfo powershell cmdlet is being called!")
client = Client(powershellbaseservername, username=proxyusername, password=proxypassword, ssl=False)
#servername = 'tul1dbapmtdb1'
#servername = request.POST.get('ServerName')
script = r"""
Import-Module SQLDBATools -DisableNameChecking;
import-module dbatools;
Get-ServerInfo '{0}' | ConvertTo-Json | Write-Output
""".format(servername)
# output, streams, had_errors = 
client.execute_ps(script)

if had_errors:
print("Error occurred in powershell script execution")
print("ERROR:\n%s" % "\n".join([str(s) for s in streams.error]))
else:
serverInfo_dict = json.loads(output)
print(serverInfo_dict['LastBootTime'])
getServerInfo = GetServerInfoForm(serverInfo_dict)

script = r"""
Import-Module SQLDBATools -DisableNameChecking;
import-module dbatools;
Get-ServerInfo '{0}'
""".format(servername)