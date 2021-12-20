import time

from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://www.spicejet.com/")
time.sleep(3)
driver.find_element_by_id("ctl00_mainContent_chk_SeniorCitizenDiscount").click()
time.sleep(3)
checkbox=driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkbox))