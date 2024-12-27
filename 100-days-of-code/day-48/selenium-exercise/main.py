from selenium import webdriver
from selenium.webdriver.common.by import By

PYTHON_URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PYTHON_URL)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].get_attribute("datetime").split("T")[0],
        "name": event_names[n].text
    }

print(events)

driver.quit()
