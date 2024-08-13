import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

cc = webdriver.ChromeOptions()

cc.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=cc)

driver.get("https://tinder.com/pt")

time.sleep(3)

bt_login = driver.find_element(By.XPATH, '//*[@id="t41619109"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
bt_login.click()
time.sleep(2)

try:
    scrooler = driver.find_element(By.XPATH, '//*[@id="t-1686761967"]/div/div[1]/div[2]/ul')
    scroll_origin = ScrollOrigin.from_element(scrooler)
    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 400) \
        .perform()

    time.sleep(1)
    bt_lang = driver.find_element(By.XPATH, '//*[@id="t-1686761967"]/div/div[1]/div[2]/ul/li[42]/a')
    bt_lang.click()

    time.sleep(1)
    bt_login = driver.find_element(By.XPATH, '//*[@id="t41619109"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
    bt_login.click()
except:
    pass
finally:
    time.sleep(1)
    bt_lg_fb = driver.find_element(By.XPATH, '//*[@id="t-1686761967"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    bt_lg_fb.click()

base_window = driver.window_handles[0]

login_window = driver.window_handles[1]
driver.switch_to.window(login_window)

time.sleep(2)

user_input = driver.find_element(By.ID, "email")
user_input.send_keys("YOUR_EMAIL")

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys("YOUR_PASSWORD")

login_fb_bt = driver.find_element(By.XPATH, '//*[@id="loginbutton"]/input')
login_fb_bt.click()

time.sleep(10)

driver.switch_to.window(base_window)

location_permiss = driver.find_element(By.XPATH, '//*[@id="t-1686761967"]/div/div[1]/div/div/div[3]/button[1]')
location_permiss.click()

time.sleep(1)

notification_permiss = driver.find_element(By.XPATH, '//*[@id="t-1686761967"]/div/div[1]/div/div/div[3]/button[2]')
notification_permiss.click()

time.sleep(5)

for i in range(100):

    time.sleep(1)

    try:

        focus_profile = driver.find_element(By.CSS_SELECTOR, 'body')
        focus_profile.send_keys(Keys.RIGHT)

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

    # like_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
    # like_button.click()
    #
    # time.sleep(2)
    #
    # try:
    #     back_to_Tinder = driver.find_element(By.XPATH, '//*[@id="t371990310"]/div/div[1]/div[1]/div/div[4]/button')
    #     back_to_Tinder.click()
    #     time.sleep(1)
    # except:
    #     pass