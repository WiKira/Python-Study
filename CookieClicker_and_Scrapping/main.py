from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com.br/dp/B0BN5WJ5V6/?coliid=I2I62YIQJCUCOB&colid=21QR94GRTW8P3&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it")
#
# value = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[6]/div[3]/div[4]/div[12]/div/div/div[3]/div[1]/span[3]/span[2]/span[2]")
#
# print(value.text)

driver.get("https://www.python.org")

values = driver.find_elements(By.CSS_SELECTOR, value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > time")
events_names = driver.find_elements(By.CSS_SELECTOR, value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a")

events = {n: {
        "time": values[n].text,
        "name": events_names[n].text
    } for n in range(len(events_names))
}

print(events)

# driver.close()
driver.quit()
