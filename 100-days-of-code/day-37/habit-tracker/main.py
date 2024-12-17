from requests import post, put, delete
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = ""

pixela_create_user_endpoint = "https://pixe.la/v1/users"
pixela_create_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
pixela_add_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
pixela_update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{datetime(year=2024, month=12, day=12).strftime("%Y%m%d")}"
pixela_delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{datetime(year=2024, month=12, day=17).strftime("%Y%m%d")}"

create_user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

create_graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ichou"
}

add_pixel_params = {
    "date": datetime.now().strftime("%Y%m%d"),
    # "date": datetime(year=2024, month=12, day=12).strftime("%Y%m%d"),
    "quantity": "12"
}

update_pixel_params = {
    "quantity": "21.30"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = post(url=pixela_create_user_endpoint, json=create_user_params)
# response = post(url=pixela_create_graph_endpoint, headers=header, json=create_graph_params)
# response = post(url=pixela_add_pixel_endpoint, headers=header, json=add_pixel_params)\
# response = put(url=pixela_update_pixel_endpoint, headers=header, json=update_pixel_params)
response = delete(url=pixela_delete_pixel_endpoint, headers=header)

print(response.text)
