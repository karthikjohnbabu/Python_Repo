import xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
driver.get("https://login.advancedmd.com/")
## Give time for iframe to load ##
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "frame-login")))
## You have to switch to the iframe like so: ##
driver.switch_to.frame(driver.find_element_by_id("frame-login"))
## Insert text via xpath ##
elem = driver.find_element_by_xpath('//input[@name="loginname"]')
elem.send_keys("johnny5")
pwd=driver.find_element_by_name('password')
pwd.send_keys('Summer@2021')
ofcky=driver.find_element_by_name('officeKey')
ofcky.send_keys('146589')
time.sleep(5)
login=driver.find_element_by_xpath("//button[@type='submit']")
login.click()
## Switch back to the "default content" (that is, out of the iframes) ##
driver.switch_to.default_content()
time.sleep(20)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
#switch on to new child window
driver.switch_to.window(window_after)
time.sleep(10)
window_after_title = driver.title
print(window_after_title)
driver.maximize_window()
driver.find_element_by_id('mnuPatientInfo').click()
time.sleep(10)
driver.switch_to.frame(driver.find_element_by_id('frmPatientInfo1'))
srch=driver.find_element_by_id('mat-input-0')
srch.send_keys('130072')
time.sleep(10)
srch.send_keys(Keys.ARROW_DOWN,Keys.ENTER)
time.sleep(10)
driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame(driver.find_element_by_id('frmPatientInfo1'))
ins=driver.find_element_by_xpath("//a[@class='left-panel-item amds-insurance-card-color'][i]")
ins.click()


