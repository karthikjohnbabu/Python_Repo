from selenium import webdriver
driver = webdriver.Ie(executable_path="C:\work\IEDriverServer_x64_3.150.1\IEDriverServer.exe")
driver.get("https://www.moneycontrol.com/")
print(driver.title)
print(driver.current_url)
driver.quit()