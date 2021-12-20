import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log=self.getLogger()
        homePage=HomePage(self.driver)
        checkoutPage=homePage.shopItems()
        log.info("Getting all the card titles")
        #homePage.shopItems().click()
        #checkOutPage=CheckOutPage(self.driver)
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
        cardText = card.text
        print(cardText)
        if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        confirmPage= checkoutPage.checkOutItems()
        log.info("Entering country name as india")
        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received from application is"+ successText)
        assert "Success! Thank you! " in successText

