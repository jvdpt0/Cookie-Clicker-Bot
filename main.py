from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
#options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
id_elements = driver.find_elements(By.CSS_SELECTOR, '#store div')
id_list = [item.get_attribute('id') for item in id_elements]

buy_time = time.time() + 5
break_time = time.time() +60*5

while True:
    cookie.click()
    if time.time() >= buy_time:
        current_cookies = int(driver.find_element(By.XPATH, '//*[@id="money"]').text.strip().replace(',',''))


        price_elements = driver.find_elements(By.CSS_SELECTOR,'#store b')
        price_elements.pop()
        price_list = [(int(element.text.split('-')[1].strip().replace(',',''))) for element in price_elements]
        
        upgrades = {id_list[i]:price_list[i] for i in range(len(price_list))}
        can_buy = {}
        for id,price in upgrades.items():
            if current_cookies > price:
                can_buy[price] = id

        max_can_buy = max(can_buy)
        print(max_can_buy)
        max_can_buy_id = can_buy[max_can_buy]
        print(max_can_buy_id)
        
        buy = driver.find_element(By.ID, max_can_buy_id).click()
        buy_time = time.time() + 5
    if time.time() >= break_time:
        cookies_per_second = driver.find_element(By.ID, "cps")
        print(cookies_per_second.text)

