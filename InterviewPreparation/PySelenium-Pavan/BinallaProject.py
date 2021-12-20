import time
from selenium import webdriver
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.maximize_window()
driver.get("https://0rloeaaqky8rq4n7-2866085953.shopifypreview.com/")
driver.find_element_by_xpath("//div[@class='icons-col flex'][a]//i[@class='ad ad-user-al']").click()
time.sleep(2)
driver.find_element_by_xpath("(//a[@href='/account/login'])[1]").click()
time.sleep(2)
driver.close()