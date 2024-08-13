import requests
import datetime as dt
import os

answer = input("Tell me which exercises did you did: ")
# answer = "ran for 15 minutes and biking for 15km"

headers = {
    "x-app-id": os.environ.get("NUTRITIONIX_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_KEY")
}

params = {
    "query": answer
}

response = requests.post(f"{os.environ.get("NUTRITIONIX_DOMAIN")}{os.environ.get("NUTRITIONIX_ENDPOINT")}", json=params, headers=headers)
data = response.json()["exercises"]

workout = {}

headers_sheety = {
    "Authorization": f"Bearer {os.environ.get("SHEETY_TOKEN")}"
}

for exercise in data:
    row = {"workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": str(exercise["name"]).title(),
            "duration": float(exercise["duration_min"]),
            "calories": float(exercise["nf_calories"])
        }
    }
    response = requests.post(os.environ.get("SHEETY_ENDPOINT"), json=row, headers=headers_sheety)
    print(response.text)
