from twilio.rest import Client
import requests

OWM_Api = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": "-22.5647",
    "lon": "-47.4017",
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url=OWM_Api, params=parameters)
response.raise_for_status()
data = response.json()["list"]

will_rain = False
for item in data:
    if item["weather"][0]["id"] < 700:
        will_rain = True
    print(f"{item["dt_txt"]} -> {item["weather"][0]["id"]}: {item["weather"][0]["main"]}, "
          f"{item["weather"][0]["description"]}.")

if will_rain:
    msg = "Leva guarda-chuva caraio. ☂️"
else:
    msg = "Vai chover não, fica suave. ☀️"

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+YOUR_TWILIO_NUMBER',
  body=msg,
  to='whatsapp:+YOUR_WHATSAPP_NUMBER'
)

print(message.status)