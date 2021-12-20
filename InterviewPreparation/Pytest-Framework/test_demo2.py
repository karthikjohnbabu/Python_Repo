import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg="Hello"
    assert msg == "Hi", "Test Failed because strings do not much"

def test_SecondCreditCard():
    a=4
    b=6
    assert a+2 == 6, " Addition do not match"

@pytest.fixture()
def setup():
    print("I will be executed first")

def test_fixtureDemo(setup):
    print("I will Executed steps in fixtureDemo Method")