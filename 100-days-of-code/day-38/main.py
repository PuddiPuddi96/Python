from requests import post
from datetime import datetime

# API LINK: https://developer.nutritionix.com/
APPLICATION_ID = ""
APPLICATION_KEY = ""

TOKEN = ""

GENDER = "MALE"
WEIGHT_KG = 83
HEIGHT_CM = 187
AGE = 28

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# https://sheety.co/
sheet_endpoint = ""

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
