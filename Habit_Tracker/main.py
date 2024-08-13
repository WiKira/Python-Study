import requests
import datetime as dt

USERNAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"
GRAPH = "YOUR GRAPH"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Study Cicle",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

# date = dt.datetime.now().strftime("%Y%m%d"),
date = dt.datetime(year=2024, month=6, day=21).strftime("%Y%m%d")

pixel_params = {
    "date": date,
    "quantity": "3.5"
}

# response = requests.post(pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

alter_pixel_ep = f"{pixel_endpoint}/{date}"

alter_param = {
    "quantity": "2.3"
}

# response = requests.put(alter_pixel_ep, json=alter_param, headers=headers)
# print(response.text)

response = requests.delete(alter_pixel_ep, headers=headers)
print(response.text)
