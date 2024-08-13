from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_counter = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

print(article_counter.text)

# article_counter.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search = driver.find_element(By.CSS_SELECTOR, "#p-search > a > span.vector-icon.mw-ui-icon-search.mw-ui-icon-wikimedia-search")
search.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# driver.quit()
