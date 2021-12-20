from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver=driver

    confirmCountry= (By.ID, "country")
    Country= (By.LINK_TEXT,"India")
    checkbox=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    submit=(By.CSS_SELECTOR,"[type='submit']")
    success=(By.CLASS_NAME,"alert-success")
    #driver.find_element_by_class_name("alert-success")


    def getconfirmCountry(self):
        return self.driver.find_element(*ConfirmPage.confirmCountry)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.Country)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.success)