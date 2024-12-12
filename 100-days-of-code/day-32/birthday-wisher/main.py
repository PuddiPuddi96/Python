from datetime import datetime
from pandas import read_csv
from random import randint
from smtplib import SMTP

NAME_PLACEHOLDER = "[NAME]"

HOTMAIL_SMTP = "smtp.live.com"
FROM_HOTMAIL_EMAIL = ""

PASSWORD = ""

def send_email(text, to):
    with SMTP(HOTMAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=FROM_HOTMAIL_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_HOTMAIL_EMAIL, 
            to_addrs=to,
            msg=f"Subject:Happy Birthday!\n\n{text}"
        )

# Get current day
today = datetime.now()
today_tuple = (today.month, today.day)

# Get data from csv
birthdays_data = read_csv("./birthdays.csv")
birthdats_dict = {(row["month"], row["day"]): row for (index, row) in birthdays_data.iterrows()}

if today_tuple in birthdats_dict:
    birthday_person = birthdats_dict[today_tuple]
    file_path = f"./letter_templates/letter_{randint(1,3)}.txt"
    with open(file=file_path, mode="r") as letter_file:
        letter_file_content = letter_file.read()
        new_letter_file_content = letter_file_content.replace(NAME_PLACEHOLDER, birthday_person["name"])
    send_email(text=new_letter_file_content, to=birthday_person["email"])
