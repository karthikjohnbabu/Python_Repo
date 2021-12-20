import requests
import sys
import pprint
import subprocess
import os

SAAD = "https://saad-ba.efi.com"

if len(sys.argv) == 2:
    issue_id = sys.argv[1]
else:
    print("Please pass the FITID ")
    sys.exit(2)

if os.environ.get('Windows_Password') == '' and os.environ.get('Windows_UserName') == '':
    print("Please Set the enironment variables  Windows_Password and Windows_UserName to conitnue")
    sys.exit(2)


def handle_response_errors(response):
    if response.status_code == 404:
        print("Not Found")
        sys.exit(404)

    if response.status_code == 401:
        print("Access Denied")
        sys.exit(401)

    if response.status_code != 200:
        print("Unhandled error: {}".format(response.status_code))
        sys.exit(response.status_code)


headers = {
    'Accept': 'application/json',
    'jira-login': os.environ['Windows_UserName'],
    'jira-password': os.environ['Windows_Password'],
    'saad-api-key': 'c0a109c2-9c81-4412-8ce8-55e743fe8215',
}

issue_url = "{saad}/api/v0/issues/{issue_id}".format(saad=SAAD, issue_id=issue_id)
response = requests.get(issue_url, headers=headers)
descJson = response.json()
print(descJson)
descr = descJson['description']
print(descr)
found = False
for logfileLocation in descr.splitlines():
    if "\\basqa" in logfileLocation or "\\10.210.68.45" in logfileLocation:
        found = True
        break
if found == True:
    print(logfileLocation)
    print(os.path.join('\\\\', logfileLocation.split('\\\\')[-1]))
else:
    print("Logs Not Found in \\basqa or \\10.210.68.45 location")

sys.exit(0)