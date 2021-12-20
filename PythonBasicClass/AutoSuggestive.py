import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://www.spicejet.com/")
time.sleep(5)
driver.find_element_by_xpath("//input[@id='ctl00_mainContent_ddl_originStation1_CTXT']").click()
driver.find_element_by_xpath("//a[@value='BLR']").click()
time.sleep(3)
driver.find_element_by_xpath("(//a[@value='MAA'])[2]").click()