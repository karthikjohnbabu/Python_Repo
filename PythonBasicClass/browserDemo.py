from selenium import webdriver

#driver= webdriver.Chrome(executable_path="C:\work\chromedriver_win32\chromedriver.exe") #chrome browser.
#driver= webdriver.Firefox(executable_path="C:\work\geckodriver-v0.26.0-win64\geckodriver.exe")# Firefox browser.
driver= webdriver.Ie(executable_path="C:\work\IEDriverServer_x64_3.150.1\IEDriverServer.exe")
driver.get("https://www.makemytrip.com/")
driver.close()