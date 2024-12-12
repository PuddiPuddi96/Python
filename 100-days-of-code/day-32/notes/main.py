from smtplib import SMTP
from datetime import datetime
from random import choice

FROM_HOTMAIL_EMAIL = ""
HOTMAIL_SMTP = "smtp.live.com"

PASSWORD = ""

GMAIL_EMAIL = ""
GMAIL_SMTP = "smtp.gmail.com"

TO_EMAIL = ""

quotes = []

def load_quotes():
    global quotes
    with open(file="./quotes.txt") as quotes_file:
        for quote in quotes_file.readlines():
            quotes.append(quote)

def get_random_quote():
    return choice(quotes)

def send_email(text):
    with SMTP(HOTMAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=FROM_HOTMAIL_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_HOTMAIL_EMAIL, 
            to_addrs=TO_EMAIL,
            msg=f"Subject:Monday motivation\n\n{text}"
        )

load_quotes()
weekday = datetime.now().weekday()
if weekday == 0: # Monday
    quote = get_random_quote()
    send_email(quote)
    
