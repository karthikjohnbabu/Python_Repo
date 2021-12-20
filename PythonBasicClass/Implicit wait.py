import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#global wait
#implicit wait will wait maximun for 5 seconds in this case
#if the element is visible within 2 seconds the web driver will resume its control.
#if the object is not visible within 5 seconds. then there will be an error. Element not found.
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(3)
buttons= driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)

