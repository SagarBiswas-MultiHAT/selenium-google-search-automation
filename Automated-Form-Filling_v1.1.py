from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.google.com')

search = browser.find_element(By.NAME, 'q')
search.send_keys("Hello, Google!")
search.send_keys(Keys.RETURN)


