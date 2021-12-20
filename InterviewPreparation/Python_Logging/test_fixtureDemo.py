import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will Executed steps in fixtureDemo Method")

    def test_fixtureDemo1(self):
        print("I will Executed steps in fixtureDemo1 Method")

    def test_fixtureDemo2(self):
        print("I will Executed steps in fixtureDemo2 Method")

    def test_fixtureDemo3(self):
        print("I will Executed steps in fixtureDemo3 Method")