import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

##############################################################################
# Initialize 
##############################################################################
# I believe there's a bug in the Python bindings with finding the Chrome
# driver, even if it's on your paht, so must pass it to constructor explicitly:
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# bring to front
driver.maximize_window()
driver.execute_script('window.focus()')

##############################################################################
# Get the page we need
##############################################################################
driver.get("http://www.python.org")


##############################################################################
# Assert stuff
##############################################################################

print "checking title"
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "Google" in driver.title

##############################################################################
# Done
##############################################################################
print "Done - closing"
driver.close()
