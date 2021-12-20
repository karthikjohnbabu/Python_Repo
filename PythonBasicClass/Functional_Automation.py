import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
list1=[]
list2=[]
driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(3)
buttons= driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list1)
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait= WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))
vegies= driver.find_elements_by_xpath("//p[@class='product-name']")
for veg in vegies:
    list2.append(veg.text)
print(list2)
assert list1==list2
originalAmount=driver.find_element_by_xpath("//span[@class='totAmt']").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
discountAmount= driver.find_element_by_xpath("//span[@class='discountAmt']").text
assert float (discountAmount)<int(originalAmount)
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)

amounts= driver.find_elements_by_xpath("//td[5]/p")
sum = 0
for amount in amounts:
    sum =sum +int(amount.text)
    print(sum)
assert sum == int(originalAmount)



