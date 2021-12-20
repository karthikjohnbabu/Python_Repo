from selenium import webdriver
from selenium.webdriver import ActionChains
chrome_options =webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
driver= webdriver.Chrome(executable_path="C:\work\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")