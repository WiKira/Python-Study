import datetime
import json
import math
import time

import data_manager
import flight_search
import notification_manager
from dotenv import load_dotenv

load_dotenv()
dt_mgr = data_manager.DataManager()
# rows = dt_mgr.get_rows()
# emails = dt_mgr.get_users_email()

with open("flight.json") as file:
    rows = json.load(file)

with open("emails.json") as file:
    emails = json.load(file)

fs = flight_search.FlightSearch()

for cities in rows["prices"]:
    if cities["iataCode"] == '':
        iata_code = fs.searchIATA(cities["city"])
        # dt_mgr.update_sheet(cities["id"], "iata_code", iata_code)
        cities["iataCode"] = iata_code
        time.sleep(1)

from_date = datetime.datetime.now() + datetime.timedelta(days=1)
to_date = datetime.datetime.now() + datetime.timedelta(days=(6*30))

not_mngr = notification_manager.NotificationManager()

for cities in rows["prices"]:
    if cities["iataCode"] is not None and cities["iataCode"] != '':
        print(cities["iataCode"])
        cheapest_flight = fs.check_flights(cities["iataCode"], from_date, to_date, cities["lowestPrice"])

        if cheapest_flight.price == 'N/A':
            cheapest_flight = fs.check_flights(cities["iataCode"], from_date, to_date, cities["lowestPrice"], "false")

        if cheapest_flight.price != 'N/A':
            not_mngr.send_message(cheapest_flight)

            not_mngr.send_email(cheapest_flight, emails)
            # dt_mgr.update_sheet(cities["id"], "lowestPrice", math.floor(cheapest_flight.price))
            cities["lowestPrice"] = math.floor(cheapest_flight.price)
        time.sleep(1)

with open("flight.json", mode="w") as file:
    json.dump(rows, file, indent=4)

