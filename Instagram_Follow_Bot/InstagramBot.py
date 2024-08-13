import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class InstagramBot:

    def __init__(self):
        cc = webdriver.ChromeOptions()
        cc.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=cc)
        self.driver.get("https://www.instagram.com")

    def login(self, username, password):
        time.sleep(5)
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(username)

        passw = self.driver.find_element(By.NAME, "password")
        passw.send_keys(password)
        time.sleep(2)
        btn_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        btn_login.click()
        time.sleep(5)
        btn_notif = self.driver.find_element(By.XPATH, '//div[contains(text(), "Agora não")]')
        btn_notif.click()
        time.sleep(5)
        btn_notif = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        btn_notif.click()

    def find_followers(self, similar_account):
        self.driver.get(f"https://www.instagram.com/{similar_account}")

        btn_followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'seguidores')
        btn_followers.click()
        time.sleep(5)

    def follow(self):
        botoes_seguir = self.driver.find_elements(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-._ap30')

        for botao in botoes_seguir:
            botao.click()
            time.sleep(30)

    def close_nav(self):
        self.driver.quit()

if __name__ == '__main__':
    pass