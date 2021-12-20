#Authentication
import requests
from requests.auth import HTTPBasicAuth

se=requests.session()
se.auth=auth=('karthikjohnbabu@gmail.com',"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")
url ='https://api.github.com/user'
github_response=requests.get(url, auth=('karthikjohnbabu@gmail.com',"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"))
print(github_response.status_code)

#How can we generalise this git hub authentication and it will be applicable to all git hub api's
#By using session manager, we can create a session for git hub API's and use that session for all our transactions in git hub API.
#what is the difference between request.get and session.get
# Session and request are of the same, where as session has the capability of authentication as well.

url2= 'https://api.github.com/user/repos'
respone=se.get(url2)
print(respone.status_code)
