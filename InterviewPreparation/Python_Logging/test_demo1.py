# Any pytest file should start with test_ or end with _test
# Pytest method names should start with test
# all the code should be wrapped inside a method.
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print('Good Morning!!!')

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
