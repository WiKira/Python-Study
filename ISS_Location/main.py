import requests
import datetime as dt
import smtplib
import time

MY_MAIL = "YOUR_EMAIL"
MY_PASS = "YOUR_PASSWORD"
MY_LAT = -22.583826
MY_LNG = -47.409771


def in_position():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    print(data)
    longitude = float(response.json()['iss_position']['longitude'])
    latitude = float(response.json()['iss_position']['latitude'])
    iss_position = (longitude, latitude)
    print(iss_position)
    return (MY_LAT - 5) <= latitude <= (MY_LAT + 5) and (MY_LNG - 5) <= longitude <= (MY_LNG + 5)


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }

    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise)
    print(sunset)

    today_hour = dt.datetime.now().hour

    return sunrise > today_hour > sunset


while True:
    if is_night() and in_position():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="YOUR_EMAIL", password="YOUR_APP_PASSWORD")
            connection.sendmail(from_addr="YOUR_EMAIL", to_addrs="YOUR_EMAIL",
                                msg=f"Subject:Look Up\n\nThe ISS is up here over your head.")
            connection.close()
    time.sleep(60)
