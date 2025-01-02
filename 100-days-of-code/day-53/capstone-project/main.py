from form_populate import FormPopulate
from scraping_data import ScrapingData

URL = "https://appbrewery.github.io/Zillow-Clone/"

scraping = ScrapingData()
formPopulate = FormPopulate(
    addresses=scraping.addresses, 
    prices=scraping.prices, 
    links=scraping.links)
formPopulate.populate()
