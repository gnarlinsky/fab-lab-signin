import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# I believe there's a bug in the Python bindings with finding the Chrome
# driver, even if it's on your paht, so must pass it to constructor explicitly:
chromedriver = "chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver




driver = webdriver.Chrome(chromedriver)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "Google" in driver.title
driver.close()
