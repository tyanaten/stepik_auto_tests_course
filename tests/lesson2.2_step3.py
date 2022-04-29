from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    x = x_element.text
    sum = int(x) + int(y)
    sum = str(sum)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
