from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

#@pytest.mark.usefixtures("setup")

from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log =self.getLogger()
        homePage=HomePage(self.driver)
        checkOutPage =homePage.shopItems()
        log.info("Getting all the Card Titles")
        cards = checkOutPage.getCardTitles()
        i=-1
        for card in cards:
            i=i+1
            cardText=card.text
            log.info(cardText)
            if cardText == "Blackberry":
               checkOutPage.getCardFooter()[i].click()
        checkOutPage.getCheckOut().click()
        confirmPage=checkOutPage.getCheckOut2()
        log.info("Entering Country Name as ind")
        confirmPage.getconfirmCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.getCountry().click()
        confirmPage.getCheckbox().click()
        confirmPage.getSubmitButton().click()
        successText = confirmPage.getSuccessText().text
        assert "Success! Thank you!" in successText
        log.info("Text Received from application is"+successText)
        self.driver.get_screenshot_as_file("screen.png")

