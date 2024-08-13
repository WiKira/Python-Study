from flight_data import FlightData
import requests
import os


class FlightSearch:

    def __init__(self):
        self._api_key = os.getenv("AMADEUS_KEY")
        self._api_secret = os.getenv("AMADEUS_SECRET")
        self._token = self._get_new_token()

    def searchIATA(self, city_name: str) -> str:
        headers = {
            "Authorization": f"Bearer {self._token}"
        }

        query = {
            "keyword": city_name,
            "subType": "CITY"
        }

        response = requests.get(
            url=f"{os.environ.get('AMADEUS_BASEURL')}/reference-data/locations",
            headers=headers,
            params=query
        )

        response.raise_for_status()
        try:
            iata_code = response.json()["data"][0]["iataCode"]
            return iata_code
        except IndexError:
            return ''

    def _get_new_token(self) -> str:

        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=f"{os.getenv("AMADEUS_BASEURL")}/security/oauth2/token",
                                 headers=header, data=body)
        response.raise_for_status()
        return response.json()["access_token"]

    def check_flights(self, destinationLocationCode, departureDate , returnDate, maxPrice, nonStop = "true"):

        headers = {
            "Authorization": f"Bearer {self._token}"
        }

        params = {
            "originLocationCode": "GRU",
            "destinationLocationCode": destinationLocationCode,
            "departureDate": departureDate.strftime("%Y-%m-%d"),
            "returnDate": returnDate.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": nonStop,
            "currencyCode": "BRL",
            "maxPrice": maxPrice
        }

        response = requests.get(
            url=os.environ.get('FLIGHT_ENDPOINT'),
            headers=headers,
            params=params
        )

        return FlightData.find_cheapest_flight(response.json())