import requests
import os


class DataManager:

    def __init__(self):
        self.endpoint = os.getenv("SHEETY_BASEURL")

    def get_rows(self):
        headers = {
            "Authorization": f"Basic {os.getenv("SHEETY_TOKEN")}"
        }
        response = requests.get(url=f"{self.endpoint}/prices", headers=headers)
        response.raise_for_status()
        return response.json()

    def update_sheet(self, row_id: str, *args):
        headers = {
            "Authorization": f"Basic {os.getenv("SHEETY_TOKEN")}"
        }

        params = {
            "price": {
                args[0]: args[1]
            }
        }
        response = requests.put(url=f"{self.endpoint}/prices/{row_id}", json=params, headers=headers)
        response.raise_for_status()
        return

    def get_users_email(self):
        headers = {
            "Authorization": f"Basic {os.getenv("SHEETY_TOKEN")}"
        }
        response = requests.get(url=f"{self.endpoint}/users", headers=headers)
        response.raise_for_status()
        return response.json()["users"]