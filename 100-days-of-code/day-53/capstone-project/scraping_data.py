from requests import get
from bs4 import BeautifulSoup
import re

URL = "https://appbrewery.github.io/Zillow-Clone/"

class ScrapingData():

    def __init__(self):
        self.addresses = []
        self.prices = []
        self.links = []
        self.__load_data()
    
    def __load_data(self):
        response = get(URL)
        html_doc = response.text
        soup = BeautifulSoup(html_doc, "html.parser")

        apartment_list =  soup.find_all("ul", {"class": "List-c11n-8-84-3-photo-cards"})
        for aparment in apartment_list:
            for address_apartment in aparment.find_all("address"):
                self.addresses.append(address_apartment.text.strip())
            for a_apartment in aparment.find_all("a"):
                link = a_apartment.get("href")
                if link not in self.links:
                    self.links.append(link)
            for price_apartment in aparment.find_all("span", {"class": "PropertyCardWrapper__StyledPriceLine"}):
                self.prices.append(re.sub('[+?mobd/]', '', price_apartment.text).split(' ')[0])
