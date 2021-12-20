from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# The next button has an attribute "aria-disabled" which turn to true when is becomes disabled
# fetching the value in nxt_btn, if the next button is enabled or disabled
nxt_btn = driver.find_element(By.XPATH, "//a[@aria-label='Next']").get_attribute("aria-disabled")
# initially taking this as false, if product will be found then we will mark it as True
is_found = False
# condition satisfies unless the nxt_btn becomes disabled (i.e attribute "aria-disabled" value will turn to true|
while nxt_btn == "false":
    products = driver.find_elements(By.XPATH, "//tbody/tr")
    for product in products:
        product_name = product.find_element(By.XPATH, ".//td[1]").text
        if product_name == "Rice":
            price = product.find_element(By.XPATH, ".//td[2]").text
            discount = product.find_element(By.XPATH, ".//td[3]").text
            print("product name:", product_name)
            print("product price:", price)
            print("product discount", discount)
            # marking is_found as True since the product has been found
            is_found = True

    # checking the condition if product is found or not, if found use break and come out of while loop, else continue
    if is_found is True:
        break
    nxt_btn = driver.find_element(By.XPATH, "//a[@aria-label='Next']").get_attribute("aria-disabled")
    if nxt_btn == "false":
        driver.find_element(By.XPATH, "//a[@aria-label='Next'][@aria-disabled='false']").click()