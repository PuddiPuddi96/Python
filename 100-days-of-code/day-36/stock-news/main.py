from requests import get
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

INCREASE_DECRESE_VALUE = 5

FROM_NUMBER = ""
TO_NUMBER = ""

account_sid = ""
auth_token = ""

up_down = None

def check_stock():
    global up_down

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }

    response = get(url=STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    data_list = [value for (key, value) in data.items()]

    last_data = data_list[0]
    last_closing_price = last_data["4. close"]
    
    before_last_data = data_list[1]
    before_last_closing_price = before_last_data["4. close"]

    difference = round(((float(last_closing_price) - float(before_last_closing_price)) / float(before_last_closing_price)) * 100, 2)
    print(difference)

    if difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    return difference >= INCREASE_DECRESE_VALUE

def send_message(text: str):
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    
    client = Client(account_sid, auth_token, http_client=proxy_client)
    
    message = client.messages.create(body=text, from_=FROM_NUMBER, to=TO_NUMBER)
    print(message.status)

def get_news():
    parameters = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "apikey": NEWS_API_KEY,
    }

    response = get(url=NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    articles = response.json()["articles"]

    first_three = articles[:3]

    formatted_articles = [f"{STOCK}:{up_down} \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in first_three]

    for article in formatted_articles:
        print(article)
        send_message(text=article)


if check_stock():
     print("Get news")
     get_news()
