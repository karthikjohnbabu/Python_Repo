
from selenium import webdriver as wd
import pytest
import time
Chrome=wd.Chrome(executable_path=r"C:\work\chromedriver.exe")
Firefox=wd.Firefox(executable_path=r"C:\work\geckodriver.exe")
class TestLogin():
    @pytest.fixture()
    def setup1(self):
        browsers=[Firefox,Chrome]
        for i in browsers:
            self.driver= i
            self.driver.get("https://www.python.org")
            time.sleep(3)
        yield
        time.sleep(3)
        self.driver.close()

    def test_Python_website(self,setup1):
        self.driver.find_element_by_id("downloads").click()
        time.sleep(3)
