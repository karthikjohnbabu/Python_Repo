import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5) #global wait.
#wait until 4 seconds if object is not displayed
#global wait
#if your object do not show up at all then max time your test waits for 4 seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
count =len(driver.find_elements_by_xpath("//div[@class='products']/div"))
time.sleep(3)
buttons= driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
driver.find_element_by_xpath("//button[text()='Place Order']").click()
dropdown=Select(driver.find_element_by_xpath("//div[@class='wrapperTwo']//div//select"))
dropdown.select_by_value("India")
driver.find_element_by_xpath("//input[@class='chkAgree']").click()
driver.find_element_by_xpath("//button[text()='Proceed']").click()
