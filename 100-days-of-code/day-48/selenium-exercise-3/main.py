from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"
LAB_REPORT_URL = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(LAB_REPORT_URL)

#---------- EXAMPLE WITH WIKIPEDIA PAGE ---------- #

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

#Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#Find the search <input> by name
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

#---------- EXERCISE ---------- #
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Davide")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Strianese")

email = driver.find_element(By.NAME, value="email")
email.send_keys("aaaa@aaa.com")

submit_button = driver.find_element(By.XPATH, value='/html/body/form/button')
# submit_button = driver.find_element(By.CSS_SELECTOR, value='form button')
submit_button.click()
