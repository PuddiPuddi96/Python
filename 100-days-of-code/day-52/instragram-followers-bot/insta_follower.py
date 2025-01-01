from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

INSTAGRAM_URL = "https://www.instagram.com/"

SIMILAR_ACCOUNT = "casaragusa"
INSTAGRAM_URL_FOLLOWERS = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers"

INSTAGRAM_USERNAME = ""
INSTAGRAM_PASSWORD = ""

class InstaFollower():

    def __init__(self):
        self.driver = self.__set_up_web_driver()

    
    def __set_up_web_driver(self):
        chrome_options = webdriver.ChromeOptions()
        
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")

        return webdriver.Chrome(options=chrome_options)
    
    def login(self):
        self.driver.get(INSTAGRAM_URL)

        sleep(2)
        cookies = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        cookies.click()

        sleep(1)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        username.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(INSTAGRAM_PASSWORD, Keys.ENTER)

        sleep(20)
        informations = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_Aa"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div')
        informations.click()
        

    def find_followers(self):
        sleep(1)
        self.driver.get(INSTAGRAM_URL_FOLLOWERS)
        sleep(2)
        
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                sleep(2)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
