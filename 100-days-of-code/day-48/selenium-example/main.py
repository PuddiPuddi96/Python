from selenium import webdriver
from selenium.webdriver.common.by import By

AMAZON_URL = "https://www.amazon.it/Sony-FE-70-2-8-GM-Lens/dp/B01BESQYJW/?_encoding=UTF8&pd_rd_w=dg48T&content-id=amzn1.sym.c60a350d-e857-4e42-bcea-c2f952e71de5%3Aamzn1.symc.36bd837a-d66d-47d1-8457-ffe9a9f3ddab&pf_rd_p=c60a350d-e857-4e42-bcea-c2f952e71de5&pf_rd_r=7SRKXQ15NE57F4PB2334&pd_rd_wg=GEOgm&pd_rd_r=12bdf8ed-8477-4dca-ab8a-e43f8f709e0e&ref_=pd_hp_d_btf_ci_mcx_mr_hp_atf_m"
PYTHON_URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PYTHON_URL)

#Example for amazon -> get the price
# price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole") #Selenium element
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The price is: {price_euro.text}.{price_cents.text} euro")

#Example for python.org -> get searchbar name
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name) # -> input
print(search_bar.get_attribute("placeholder")) # -> search

#Example for python.org -> get button
button = driver.find_element(By.ID, value="submit")
print(button.size)

#Example for python.org -> get link by css selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

#Example for python.org -> get link by XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close() #For a single tab (element name)
driver.quit()
