from selenium import webdriver
from selenium.webdriver.common.by import By

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(WIKIPEDIA_URL)

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

driver.quit()
