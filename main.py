import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get('https://www.issuewire.com/stockvideosorg-explains-the-importance-of-using-stock-videos-for-business-marketing-1725459559464996?fbclid=IwAR3GJrMOUcFGkohVfRkGxS-Yid5BIg9O__86Q44VVrlBiDZ5WpPuyLST8rw')
xpath = '/html/body/div[2]/div/div[2]/div[4]/blockquote/small[3]/a'

try:
    browser.implicitly_wait(30)
    button = browser.find_element("xpath", xpath)
    res = button.click()
    time.sleep(10)
    browser.close()
    print("Link is clicked!")
except NoSuchElementException:
    print("Have not element")

