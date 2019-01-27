#! /usr/bin/env python


import time     # Used for to give time for a page to load
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Setup the options for Chrome:
options = webdriver.ChromeOptions()
options.add_argument("--test-type")

# Replace this with the path to your chromedriver:
driver = webdriver.Chrome("/Users/alanmurphy/Downloads/chromedriver")

# Test on (412x732)

driver.maximize_window()

# Navigate to hostelworld.com
driver.get("https://www.hostelworld.com/")

# Find Search Box and click it:
element = driver.find_element(By.NAME, "search_keywords")
element.click()

# Type City in box
element.send_keys("Dublin")
time.sleep(5)

# Select Dublin, Ireland from predictive text drop down
element = driver.find_element(By.CLASS_NAME, "hover")
element.click()

# Click 'Let's Go!' button
element = driver.find_element(
    By.CLASS_NAME, "btn")
element.click()

# Wait for results to load and select 'Sort'
time.sleep(5)
element = driver.find_element_by_xpath(
    "//*[@class='topfilter rounded sort-button']").click()

# Click 'Name' to sort by name
time.sleep(5)
element = driver.find_element_by_id("sortByName")
element.click()


# Wait 5 seconds so you can see what has been done:
time.sleep(5)

# Test on (768x1024)

driver.set_window_size(768, 1024)

# Navigate to hostelworld.com
driver.get("https://www.hostelworld.com/")

# Find Search Box and click it:
element = driver.find_element(By.NAME, "search_keywords")
element.click()

# Type City in box
element.send_keys("Dublin")
time.sleep(5)

# Select Dublin, Ireland from predictive text drop down
element = driver.find_element(By.CLASS_NAME, "hover")
element.click()

# Click 'Let's Go!' button
element = driver.find_element(
    By.CLASS_NAME, "btn")
element.click()

# Wait for results to load and select 'Sort'
time.sleep(5)
element = driver.find_element_by_xpath(
    "//*[@class='topfilter rounded sort-button']").click()

# Click 'Name' to sort by name
time.sleep(5)
element = driver.find_element_by_id("sortByName")
element.click()


# Wait 5 seconds so you can see what has been done:
time.sleep(5)


# Test on (412x732)

driver.set_window_size(412, 732)

# Navigate to hostelworld.com
driver.get("https://www.hostelworld.com/")

# Find Search Box and click it:
element = driver.find_element(By.NAME, "search_keywords")
element.click()

# Type City in box
element.send_keys("Dublin")
time.sleep(5)

# Select Dublin, Ireland from predictive text drop down
element = driver.find_element(By.CLASS_NAME, "hover")
element.click()

# Click 'Let's Go!' button
element = driver.find_element(
    By.CLASS_NAME, "btn")
element.click()

# Wait for results to load and select 'Sort'
time.sleep(5)
element = driver.find_element_by_xpath(
    "//*[@class='sort-button']").click()

# Click 'Name' to sort by name
time.sleep(5)
element = driver.find_element_by_id("sortByName")
element.click()


# Wait 5 seconds so you can see what has been done:
time.sleep(5)

# Close the session and browser:
driver.close()
