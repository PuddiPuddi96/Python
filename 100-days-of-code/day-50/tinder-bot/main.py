from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

URL = "http://www.tinder.com"

FACEBOOK_USERNAME = ""
FACEBOOK_PASSWORD = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sleep(1)
login = driver.find_element(By.XPATH, value='//*[@id="q2098069830"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login.click()

sleep(1)
facebbok_login = driver.find_element(By.XPATH, value='//*[@id="q369688754"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
facebbok_login.click()

#Switch to facebook window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

sleep(1)
reject_cookies = driver.find_element(By.XPATH, value='//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div[1]/div/span/span')
reject_cookies.click()

sleep(1)
username = driver.find_element(By.ID, value='email')
username.send_keys(FACEBOOK_USERNAME)

password = driver.find_element(By.ID, value='pass')
password.send_keys(FACEBOOK_PASSWORD, Keys.ENTER)

#Switch to Tinder window
sleep(5)
driver.switch_to.window(base_window)

#Allow location
location = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location.click()

#Disallow notifications
notifications = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(2)
    try:
        heart_icon = driver.find_element(By.XPATH, value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button")
        heart_icon.click()

    # For "It's a match" pop-up!
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        # For "Tinder Gold" pop-up
        except NoSuchElementException:
            close_tinder_gold = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div[2]/div[2]/button")
            close_tinder_gold.click()

    # If the Like button changes XPath after the first Like
    except NoSuchElementException:
        try:
            heart_icon = driver.find_element(By.XPATH, value="//*[@id='t2067052097']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
            heart_icon.click()
        # For "Add Tinder to your Home Screen" pop-up
        except ElementClickInterceptedException:
            not_interested_button = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div/div[2]/button[2]/div[2]/div[2]/div")
            not_interested_button.click()

driver.quit()
