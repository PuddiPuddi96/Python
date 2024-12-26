from requests import get
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
import os

AMAZON_CLONE_URL = "https://appbrewery.github.io/instant_pot/"
AMAZONE_REAL_URL = "https://www.amazon.it/Mixroom-Portatile-Custodia-Computer-Notebook/dp/B09QZ383VM/?_encoding=UTF8&pd_rd_w=lu3pG&content-id=amzn1.sym.94e1c6c5-9320-40f2-aa14-4fdda82012f7&pf_rd_p=94e1c6c5-9320-40f2-aa14-4fdda82012f7&pf_rd_r=66D0BQQY48EPFRKHAXQE&pd_rd_wg=UX9af&pd_rd_r=dddef742-ddfc-4528-9434-38666d70c6e4&ref_=pd_hp_d_btf_gcx-xmas-smb-p13n"
HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
PRICE_TARGET = 100.00

load_dotenv()

def send_email(title: str, price: float, link: str):
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSOWRD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{link}".encode("utf-8")
        )


response = get(AMAZONE_REAL_URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

#Get the product price
price_span = soup.find(name="span", class_="aok-offscreen")
price = price_span.getText().split("€")[0].strip().replace(",", ".")
# price = price_span.getText().split("$")[1]
price_as_float = float(price)

#Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_as_float < PRICE_TARGET:
    send_email(title, price_as_float, AMAZON_CLONE_URL)
