#Any pytest file should start with test_ or end with _test
#pytest method names also should start with test
#Any code should be wrapped in method only.
#note: In pytest every method is treated as a test case
# -v stands for more info or metadata, -s stands for logs in output. -k stands for method names execution
# this particular test case will run,but it will not report pass or fail in the command prompt

import pytest
@pytest.fixture()
def test_firstProgram(setup):
    print("hello")


@pytest.mark.xfail
def test_greetCreditCard():
    print("Good evening")

def test_crowssBrowser(crossBrowser):
    print(crossBrowser)