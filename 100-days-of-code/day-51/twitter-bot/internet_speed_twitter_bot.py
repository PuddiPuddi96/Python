from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

TWITTER_URL = "https://x.com/home"
SPEEDTEST_URL = "https://www.speedtest.net/"

TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
TWITTER_USERNAME = ""

class InternetSpeedTwitterBot():

    def __init__(self, promise_down: float, promise_up: float):
        self.down = 0
        self.promise_down = promise_down
        self.up = 0
        self.promise_up = promise_up
        self.driver = self.__set_up_web_driver()
    

    def __set_up_web_driver(self):
        chrome_options = webdriver.ChromeOptions()
        
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")

        return webdriver.Chrome(options=chrome_options)
    
    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        
        sleep(2)
        cookies = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-reject-all-handler"]')
        cookies.click()
        
        go_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        sleep(50)
        
        up_element = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = float(up_element.text)
        
        down_element = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = float(down_element.text)

    def tweet_as_provider(self):
        self.driver.get(TWITTER_URL)
        
        sleep(3)
        login_in_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[3]/a/div/span/span')
        login_in_button.click()

        sleep(2)
        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        next_button.click()

        sleep(2)
        username = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME, Keys.ENTER)
        
        sleep(1)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        sleep(3)
        post_box = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        text = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {self.promise_down}down/{self.promise_up}up?"
        post_box.send_keys(text)

        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        post_button.click()

        self.driver.quit()
