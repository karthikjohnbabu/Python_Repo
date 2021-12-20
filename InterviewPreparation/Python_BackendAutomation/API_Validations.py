import requests
import json
response= requests.get("http://216.10.245.166/Library/GetBook.php",
             params={"AuthorName":"Rahul Shetty"},)
json_response=response.json()
print(type(json_response))
print(json_response[0]['isbn'])
assert response.status_code==200
print(response.headers) #headers are returned as dictionary.
assert response.headers['Content-Type']=='application/json;charset=UTF-8'
# retrieve the book details with ISBN RGHCC
for actualbook in json_response:
    if actualbook['isbn']=='Seyn':
        print(actualbook)
        break
expectedBook={
        "book_name": "Devops",
        "isbn": "Seyn",
        "aisle": "75"
    }

print(actualbook)
print(expectedBook)
assert actualbook == expectedBook



