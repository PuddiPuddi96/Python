import requests
from datetime import datetime
from time import sleep
from smtplib import SMTP

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

SMPT_LIVE = "smtp.live.com"
FROM_EMAIL = ""
PASSWORD = ""
TO_EMAIL = ""

def check_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and  MY_LONG - 5 <= iss_longitude <= MY_LONG + 5

def check_is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    
    return sunset <= time_now.hour or sunrise >= time_now.hour

def send_email():
    with SMTP(SMPT_LIVE) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL, 
            to_addrs=TO_EMAIL,
            msg="Subject:Look up☝\n\nThe ISS is above you in the sky"
        )

while True:
    if check_iss_position() and check_is_dark():
        send_email()
    sleep(60000)
