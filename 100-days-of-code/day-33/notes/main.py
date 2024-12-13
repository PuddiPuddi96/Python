from requests import get
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
    
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# position = (longitude, latitude)
# print(position)

parameters = {
    "lat": 41.902782,
    "lng": 12.496365,
    "formatted": 0
}

response = get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_date = sunrise.split("T")[0]
sunrise_time = sunrise.split("T")[1]
sunrise_time_split = sunrise_time.split(":")

sunset_date = sunset.split("T")[0]
sunset_time = sunset.split("T")[1]
sunset_time_split = sunset_time.split(":")

time_now = datetime.now()
