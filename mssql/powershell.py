from pypsrp.client import Client
import json
import time
import random
from SQLDBAToolsInventory_EnvironmentSettings import powershellbaseservername,proxyusername,proxypassword

client = Client(powershellbaseservername, username=proxyusername, password=proxypassword, ssl=False)

timestr = time.strftime("%Y%m%dT%H%M%S")
jsonfilepath = 'serverinfo_'+timestr+'_'+str(random.randint(1, 1000))+'.json'
servername = 'tul1dbapmtdb1'
script = r"""
Import-Module SQLDBATools -DisableNameChecking;
import-module dbatools;
Get-ServerInfo '{0}' | ConvertTo-Json | Write-Output
""".format(servername)
# Get-ServerInfo '{0}' | ConvertTo-Json | Out-File '{1}'

output, streams, had_errors = client.execute_ps(script)

if had_errors:
    print("Error occurred in powershell script execution")
    print("ERROR:\n%s" % "\n".join([str(s) for s in streams.error]))
else:
    my_dict = json.loads(output)
    print(my_dict['ServerName'])

# print(my_dict['ServerName'])
# print("HAD ERRORS: %s" % had_errors)
# print("OUTPUT:\n%s" % output)
# print("ERROR:\n%s" % "\n".join([str(s) for s in streams.error]))
# print("DEBUG:\n%s" % "\n".join([str(s) for s in streams.debug]))
# print("VERBOSE:\n%s" % "\n".join([str(s) for s in streams.verbose]))


# json_data = open('E:\\Django\SQLDBAToolsInventory\media\\json\\tempoutput01.json')
# data1 = json.load(json_data) # deserialises it
# data2 = json.dumps(json_data) # json formatted string

# json_data.close()

# data = open('E:\\Django\SQLDBAToolsInventory\media\\json\\tempoutput01.json',
#             "r", encoding="utf16").read()
# my_dict = json.loads(data)
# print(my_dict)
# my_dict['ServerName']
