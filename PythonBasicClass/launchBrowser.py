from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://www.moneycontrol.com/")
driver.maximize_window()
driver.refresh()
print(driver.title)
print(driver.current_url)
driver.close()