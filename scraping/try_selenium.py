from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
print elem
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "Google" in driver.title
