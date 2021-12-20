from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver= driver

    shop=(By.CSS_SELECTOR,"a[href*='shop']")
    name=(By.CSS_SELECTOR,"input[name='name']")
    email=(By.NAME,"email")
    checkbox=(By.ID,"exampleCheck1")
    gender=(By.ID,"exampleFormControlSelect1")
    submit=(By.CSS_SELECTOR,"input[value='Submit']")
    success=(By.CSS_SELECTOR,"div[class*='alert-success']")

    #div[class*='alert-success']"

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.success)
