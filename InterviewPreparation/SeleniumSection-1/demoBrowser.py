from selenium import webdriver
#browser Exposes an executable file
#Through Selenium Test we need to invoke the executable file
#which will then invoke actual browser.
#driver= webdriver.Chrome("C:\work\chromedriver.exe")
driver= webdriver.Firefox(executable_path="C:\work\geckodriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")#get method to hit url on the browser.
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()