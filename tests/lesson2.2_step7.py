from selenium import webdriver
import time
import math
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("input[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("input[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input[name='email']")
    input3.send_keys("pochta@m.ru")

    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
