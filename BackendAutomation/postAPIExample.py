import requests
import configparser
from payLoad import *
from utilities.resources import*
from utilities.configurations import*
# here post http method arguments are url,data, Here data we will send in the form of json payload.
# in get http method data is sent in the form of params.
url=getConfig()['API']['endpoint']+ApiResponses.addBook
headers={"Content-Type": "application/json"}
addBook_response = requests.post(url,json=addBookPayload("karth"),headers=headers, )
print(addBook_response.json())
response_json = addBook_response.json()
bookID = response_json['ID']
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json=
{

    "ID": bookID

}, headers={"Content-Type": "application/json"}, )
# assert response_deleteBook.status_code==200
res_json = response_deleteBook.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

#Authentication.
url="https://api.github.com/user"
github_response= requests.get(url,auth=("karthikjohnbabu@gmail.com",getPassword()))
print(github_response.status_code)