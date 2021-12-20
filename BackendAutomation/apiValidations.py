import json
import requests
#in get HTTP method the url and parameters are seperated using a question mark.
#the get method accepts params/parameter as a dictionary
response= requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty'},)
# print(response.text)
# print(type(response.text))
# dict_response =json.loads(response.text)
# print(dict_response[0]['isbn'])
json_response =response.json()
print(type(json_response))
print(json_response)
print(json_response[0]['isbn'])
print(response.status_code)
assert response.status_code ==200
print(response.headers)# Here headers are returned as dictionary.
assert response.headers['Content-Type']=='application/json;charset=UTF-8'
#retrieve the book details with ISBN RGHCC
for actualBook in json_response:
    if actualBook['isbn']=='RGHCC':
        print(actualBook)
        break
expectedBook= { "book_name": "Learn API Automation with RestAssured",
        "isbn": "RGHCC",
        "aisle": "12239"}
assert actualBook == expectedBook

