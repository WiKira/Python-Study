from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com")

inputs = driver.find_elements(By.CSS_SELECTOR, "input.form-control")

inputs[0].send_keys("YOUR NAME", Keys.TAB)
inputs[1].send_keys("YOUR SURNAME", Keys.TAB)
inputs[2].send_keys("YOUR EMAIL", Keys.TAB, Keys.ENTER)


# button = driver.find_element(By.CSS_SELECTOR, "button.btn")
# button.click()
