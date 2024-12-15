import os

from requests import get
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = "11d855f0e97fd09d8384fc18e10f89f7"
account_sid = ""
auth_token = ""

FROM_NUMBER = ""
TO_NUMBER = ""
MESSAGE_TEXT = "It's going to rain today. Remember to bring an umbrella"

parameters = {
    "lat": 40.608768,
    "lon": 14.983030,
    "appid": api_key,
    "cnt": 4
}

response = get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

#Single code
# print(data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # For pythoanywhere
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    
    client = Client(account_sid, auth_token, http_client=proxy_client)
    
    message = client.messages.create(body=MESSAGE_TEXT, from_=FROM_NUMBER, to=TO_NUMBER)
    print(message.status)
