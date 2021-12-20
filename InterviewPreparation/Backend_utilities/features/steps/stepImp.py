import requests
from behave import *
import configparser
from Backend_utilities.resources import APIResources


@given('the Book details which needs to be added to Library')
def step_imp(context):
    url = config['API']['endpoint'] + APIResources.addBook
    headers = {"Content-Type": "application/json"}

@when('we execute the AddBook PostAPI method')
def step_impl(context):
    addBook_response = requests.post(url, json=BuildPayLoadFromDb(query), headers=headers, )

@then('book is successfully added')
def step_impl(context):
    response_json = addBook_response.json()
    print(response_json)
    bookID = response_json['ID']
    print(bookID)
    assert response_json["Msg"] == "successfully added"