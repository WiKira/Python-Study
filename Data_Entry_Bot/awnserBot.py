import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from scraper import Scraper


class AwnserBot():

    def __init__(self, scraper: Scraper):
        self.scraper = scraper

        cc = webdriver.ChromeOptions()
        cc.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=cc)
        self.driver.get("YOUR_GOOGLE_FORM_LINK")

    def send_data(self):

        for i in range(len(self.scraper.links)):
            time.sleep(5)

            address_awnser = self.driver.find_element(By.CSS_SELECTOR, "textarea.KHxj8b.tL9Q4c")
            address_awnser.send_keys(self.scraper.addresses[i])

            price_awnser = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_awnser.send_keys(self.scraper.values[i])

            link_awnser = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_awnser.send_keys(self.scraper.links[i])

            send_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            send_button.click()

            time.sleep(5)

            send_another = self.driver.find_element(By.CSS_SELECTOR, 'body > div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > div > div.c2gzEf > a')
            send_another.click()

        self.driver.quit()