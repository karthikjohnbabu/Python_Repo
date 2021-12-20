import xlrd
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#to launch the URL and Login Module
driver.get("https://gocode.azurewebsites.net/login")
driver.find_element_by_name('email').send_keys('kmaheshbabu')
driver.find_element_by_name("password").send_keys('*Ng50j0r')
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(10)
#Script to select the module settings
driver.find_element_by_xpath('//img[@src="assets/clientcode/execassist/logo/SETUP.png"]').click()
time.sleep(5)
driver.find_element_by_xpath("//span[contains(text(),'Settings')]").click()
driver.find_element_by_xpath("//span[contains(text(),'Users')]").click()
time.sleep(5)
driver.find_element_by_xpath('//input[@placeholder="Filter by all columns"]').send_keys('kmaheshbabu')
driver.find_element_by_xpath('//button[@title="Edit"]').click()
time.sleep(15)
#Fecthing Data from Excel Sheet
file_location="Sample_Data.xls"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
a=sheet.cell_value(1,0)

#Keying the feteched value from Excel to application.
driver.find_element_by_xpath('(//input[@id="address"])[2]').send_keys(a)
driver.find_element_by_xpath('//tbody/tr[2]/th[1]/div[1]/div[2]/button[1]').click()
time.sleep(10)
driver.save_screenshot("image.png")