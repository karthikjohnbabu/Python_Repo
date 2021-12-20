import time
from selenium import webdriver
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.expedia.co.in/")
driver.maximize_window()
driver.find_element_by_xpath("//span[contains(text(),'Flights')]").click()
time.sleep(2) # from python
driver.find_element_by_xpath("//button[@data-stid='location-field-leg1-origin-menu-trigger']").send_keys("NYC")
Arr_countries= driver.find_elements_by_xpath("//li[@data-stid='location-field-leg1-origin-result-item']/button/div/div/span")
print(len(Arr_countries))
for country in Arr_countries:
    if country.text=="New York (NYC - All Airports)":
        country.click()
        break
driver.find_element_by_xpath("//button[@data-stid='location-field-leg1-destination-menu-trigger']").send_keys("DEL")
Des_countries= driver.find_elements_by_xpath("//li[@data-stid='location-field-leg1-destination-result-item']/button/div/div/span")
print(len(Des_countries))
for country in Des_countries:
    if country.text=="Delhi (DEL - Indira Gandhi Intl.)":
        country.click()
        break
driver.find_element_by_xpath("//button[@data-name='d1']").click()
time.sleep(3)
driver.find_element_by_xpath("//button[@aria-label='25 Sep 2021']").click()
driver.find_element_by_xpath("//button[@data-stid='apply-date-picker']").click()
driver.find_element_by_xpath("//button[@data-name='d2']").click()
time.sleep(3)
driver.find_element_by_xpath("//button[@aria-label='25 Oct 2021']").click()
driver.find_element_by_xpath("//button[@data-stid='apply-date-picker']").click()
driver.find_element_by_xpath("//button[@data-testid='submit-button']").click()
