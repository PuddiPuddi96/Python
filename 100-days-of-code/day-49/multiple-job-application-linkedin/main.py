from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

EMAIL = ""
PASSWORD = ""
PHONE = ""

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true"


def abort_application():
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    sleep(1)
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


sleep(1)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()


sleep(1)
login = driver.find_element(by=By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
login.click()


sleep(1)
email = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
email.send_keys(EMAIL)

password = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)


# Get Listings
sleep(2)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    listing.click()
    sleep(1)
    try:
        apply = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply.click()

        sleep(3)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            continue
        else:
            submit.click()

        sleep(2)
        close = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

sleep(5)
driver.quit()
