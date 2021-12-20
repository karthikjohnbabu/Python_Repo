#attachements.
import requests
url="https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files={'file':open('/Users/karthikbabu/Documents/279-2791029_python-icon-python-logo.png','rb')}
r=requests.post(url,files=files)
print(r.status_code)
print(r.text)