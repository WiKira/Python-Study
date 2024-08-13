import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)

lang = driver.find_element(By.ID, "langSelect-PT-BR")
lang.click()

time.sleep(5)

cookie = driver.find_element(By.ID, "bigCookie")

while True:
    cookie.click()
    time.sleep(0.01)
    enables = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
    if len(enables) > 0:
        for item in enables:
            item.click()
            time.sleep(0.1)

    enables = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    if len(enables) > 0:
        for item in enables:
            item.click()
            time.sleep(0.1)