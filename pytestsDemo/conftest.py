import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executed first") #used to invoke the browser
    yield
    print("I will be executed last")# used to close the browser and clear the cache memory of the browser.

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return["karthik","Babu","learnwithkarthik"]

@pytest.fixture(params=[("chrome","karthik"),("firefox","Babu"),("IE","SS")])
def crossBrowser(request):
    return request.param