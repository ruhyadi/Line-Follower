# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("http://192.168.4.1")

# get element
element = driver.find_element_by_id("turnleft")

while True:
    # click the element
    element.click()
