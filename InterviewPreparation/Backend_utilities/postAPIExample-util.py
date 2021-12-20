# Requirement is to add the book and delete the book.
import requests
import configparser

from Backend_utilities.configurations import getConfig
from Backend_utilities.resources import APIResources
from Python_BackendAutomation.payLoads import addBookPayload, BuildPayLoadFromDb

config=getConfig()
url=config['API']['endpoint']+ APIResources.addBook
headers={"Content-Type":"application/json"}
query= 'select * from Books3'
addBook_response= requests.post(url,json=BuildPayLoadFromDb(query),headers=headers,)
response_json=addBook_response.json()
print(response_json)
bookID=response_json['ID']

url2=config['API']['endpoint']+ APIResources.deleteBook
response_deleteBook= requests.post(url2,json={
"ID" : bookID
},headers={"Content-Type":"application/json"})
assert response_deleteBook.status_code == 200
res_json= response_deleteBook.json()
print(res_json["msg"])
assert res_json["msg"]=="book is successfully deleted"

