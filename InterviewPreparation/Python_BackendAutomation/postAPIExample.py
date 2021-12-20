# Requirement is to add the book and delete the book.
import requests
import configparser

from Python_BackendAutomation.payLoads import addBookPayload

config=configparser.ConfigParser()
config.read("Backend_utilities/properties.ini")
addBook_response= requests.post(config['API']['endpoint']+"/Library/Addbook.php",
                                json=addBookPayload("ABCDEFG"),
                                headers={"Content-Type":"application/json"},)
response_json=addBook_response.json()
bookID=response_json['ID']

response_deleteBook= requests.post('http://216.10.245.166/Library/DeleteBook.php',json={

"ID" : bookID

},headers={"Content-Type":"application/json"})
assert response_deleteBook.status_code == 200

res_json= response_deleteBook.json()
print(res_json["msg"])
assert res_json["msg"]=="book is successfully deleted"

