from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
driver.find_element_by_id("username").send_keys("karthikjohnbabu")
driver.find_element_by_name("pw").send_keys("Password")
driver.find_element_by_xpath("//*[@id='Login']").click()
print(driver.find_element_by_css_selector("#error").text)