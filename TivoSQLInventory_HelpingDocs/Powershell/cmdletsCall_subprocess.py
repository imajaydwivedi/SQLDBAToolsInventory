import subprocess
import json

#servername = "tul1cipedb2"
servername = "tul1dbapmtdb1"
ps_cmdlet = """
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process -Force;
Import-Module SQLDBATools -DisableNameChecking;
Get-ServerInfo {0} | ConvertTo-Json | Write-Output;
""".format(servername)

p = subprocess.Popen('powershell.exe '+ps_cmdlet,stdout=subprocess.PIPE)
output = p.communicate()
serverInfo_dict = json.loads(output)
# subprocess.Popen('powershell.exe '+ps_cmdlet)
#subprocess.Popen(ps_cmdlet)