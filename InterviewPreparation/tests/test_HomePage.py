import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,GetData):
        log = self.getLogger()
        # driver.find_element_by_name("name").send_keys("Karthik")
        homepage =HomePage(self.driver)
        log.info("First Name"+GetData["firstname"])
        homepage.getName().send_keys(GetData["firstname"])
        homepage.getEmail().send_keys(GetData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(),GetData["gender"])
        homepage.getSubmit().click()
        message = homepage.getSuccess().text
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def GetData(self, request):
        return request.param
