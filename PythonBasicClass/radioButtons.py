import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://parabank.parasoft.com/parabank/admin.htm")
radioButtons= driver.find_elements_by_xpath("//input[@type='radio']")
print(len(radioButtons))
for radiobutton in radioButtons:
    if radiobutton.get_attribute("value")=="soap":
        radiobutton.click()
        assert radiobutton.is_selected()
        time.sleep(3)
driver.quit()