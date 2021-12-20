import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://gocode.azurewebsites.net/login")
driver.find_element_by_name('email').send_keys('kmaheshbabu')
driver.find_element_by_name("password").send_keys('*Ng50j0r')
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(20)
driver.find_element_by_xpath("//img[@src='assets/clientcode/execassist/logo/CHCOD.png']").click()
time.sleep(10)
driver.find_element_by_xpath("//a[@title='Operations']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(),'Modify PDs')]").click()
driver.find_element_by_id('pan').send_keys('11223344')