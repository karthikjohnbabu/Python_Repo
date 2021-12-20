from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
browser = webdriver.Firefox(executable_path="C:\work\geckodriver.exe")
browser.maximize_window()
browser.get("https://twitter.com/")
print(browser.title)
print(browser.current_url)
browser.get("https://www.moneycontrol.com/")
print(browser.title)
print(browser.current_url)
browser.back()
browser.refresh()


