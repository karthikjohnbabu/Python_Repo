import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first") # used to invoke the browser, before test case execution necessary setup
    yield
    print(" I will be executed at last") # used to clean up the session, post running the test case


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return["Karthik","Babu","karthikjohnbabu@gmail.com"]

@pytest.fixture(params=[("chrome","Rahul","Shetty"),("Firefox","shetty"),("IE","SS")])
def crossBrowser(request):
    return request.param