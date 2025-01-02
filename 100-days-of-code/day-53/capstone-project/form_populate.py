from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeufCp2edjQ1U-GyTBiWj8f_bFiLgzrTwx2Lu4moKoKXLvxSw/viewform?usp=header"


class FormPopulate():

    def __init__(self, addresses: list, links: list, prices: list):
        self.driver = self.__set_up_web_driver()
        self.addresses = addresses
        self.links = links
        self.prices = prices
    
    def __set_up_web_driver(self):
        chrome_options = webdriver.ChromeOptions()
        
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")

        return webdriver.Chrome(options=chrome_options)

    def populate(self):
        for num in range (len(self.addresses)):
            sleep(1)
            self.driver.get(GOOGLE_FORM_URL)

            sleep(1)
            address = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(self.addresses[num])

            price = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(self.prices[num])

            link = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link.send_keys(self.links[num])

            self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
        
        self.driver.quit()
