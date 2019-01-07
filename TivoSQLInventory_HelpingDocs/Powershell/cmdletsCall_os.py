import os
import json

servername = "tul1cipedb2"
#servername = "tul1dbapmtdb1"
ps_cmdlet = """
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process -Force;
Import-Module SQLDBATools -DisableNameChecking;
Get-ServerInfo {0};
""".format(servername)

os.system('powershell.exe '+ps_cmdlet)