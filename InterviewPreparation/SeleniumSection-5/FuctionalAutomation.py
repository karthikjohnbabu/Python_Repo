#Two types of waits available.
#1. Implicit Wait
#2. Explicit Wait
#Pause the test for few seconds using Time class.
import time
from selenium import webdriver
list=[]
list2=[]
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.implicitly_wait(5)
#wait until 5 seconds if object is not displayed. And this wait is applied globally to all the statements.
#Implicit wait is called as global wait. It is smart wait.
#if the web element loads in 1.5 second, then execution will resume immediately. It will not waste time for 5 seconds.
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count==3
buttons= driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(4)
vegies= driver.find_elements_by_xpath("//p[@class='product-name']")
for veg in vegies:
    list2.append(veg.text)
print(list2)
assert list == list2
OriginalAmount= driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
DiscountAmount= driver.find_element_by_css_selector(".discountAmt").text
assert float(DiscountAmount)<float(OriginalAmount)
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum=0
for amount in amounts:
   sum= sum+ int(amount.text)
print(sum)
totalAmount=int(driver.find_element_by_class_name("totAmt").text)
assert sum==totalAmount