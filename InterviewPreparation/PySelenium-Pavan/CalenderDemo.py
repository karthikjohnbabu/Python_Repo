import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script("document.querySelector('.tableFixHead').scrollTop=5000")
tableData= driver.find_elements_by_css_selector(".tableFixHead td:nth-child(4)")
sum=0
for data in tableData:
   sum = sum+int(data.text)
string= driver.find_element_by_class_name("totalAmount").text
list = string.split(":")
print(list)
actualAmt=int(list[1])
print(actualAmt)
assert actualAmt==sum


