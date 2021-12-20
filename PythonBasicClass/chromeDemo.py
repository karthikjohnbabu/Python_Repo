from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe")
driver.get("https://www.moneycontrol.com/")
print(driver.title)
print(driver.current_url)
driver.close() # only close the current window.
driver.quit() #all the tabs and windows will be closed.
