import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3951175455&f_AL=true&f_E=3&geoId=106057199&keywords=analista%20de%20dados&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")
time.sleep(1)

try:
    loginButton = driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")
    loginButton.click()
    time.sleep(1)

    username = driver.find_element(By.ID, "username")
    username.send_keys("YOUR_USERNAME")

    password = driver.find_element(By.ID, "password")
    password.send_keys("YOUR_PASSWORD")

    loginSender = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    loginSender.click()
except:
    pass


n_vagas = 0

while True:
    job_panel = driver.find_elements(By.CSS_SELECTOR, ".artdeco-entity-lockup__title.ember-view > a")

    if len(job_panel) <= n_vagas:
        break

    n_vagas = len(job_panel)

    for job_link in job_panel:
        try:
            job_link.click()
            time.sleep(1)

            save_button = driver.find_element(By.CSS_SELECTOR, "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div:nth-child(1) > div.mt5 > div > button")

            button_span = save_button.find_element(By.CSS_SELECTOR, "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div:nth-child(1) > div.mt5 > div > button > span:nth-child(1)")

            scrooler = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results-list")
            scroll_origin = ScrollOrigin.from_element(scrooler)
            ActionChains(driver) \
                .scroll_from_origin(scroll_origin, 0, 200) \
                .perform()

            if button_span.text == "Salvos":
                continue

            save_button.click()
            time.sleep(1)
        except:
            continue
