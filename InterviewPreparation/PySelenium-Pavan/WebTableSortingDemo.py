import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element_by_xpath("//tr/th[1]").click()
elements =driver.find_elements_by_xpath("//tbody/tr/td[1]")
ol=[]
for element in elements:
    a=element.text
    ol.append(a)
print(ol)
ol.sort()
print(ol)
