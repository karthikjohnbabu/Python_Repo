from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver= driver
    #driver.find_elements_by_xpath("//div[@class='card h-100']")
    cardTitle =(By.CSS_SELECTOR,".card-title a")
    cardFooter=(By.CSS_SELECTOR,".card-footer button")
    checkOut=(By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkOut_2=(By.CSS_SELECTOR,"button[class*='btn-success']")

    #self.driver.find_element_by_css_selector("button[class*='btn-success']")



    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getCheckOut(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def getCheckOut2(self):
        self.driver.find_element(*CheckOutPage.checkOut_2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage