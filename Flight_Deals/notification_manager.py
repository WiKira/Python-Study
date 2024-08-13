import os
import smtplib
from twilio.rest import Client

import flight_data


def create_message(cheapest_flight: flight_data.FlightData):
    return (f"Low Price Alert! Only R${cheapest_flight.price} to fly "
            f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
            f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")


class NotificationManager:

    def __init__(self):
        self.account_sid = os.getenv("TWILIO_SID")
        self.auth_token = os.getenv("TWILIO_TOKEN")
        self.number_from = os.getenv("TWILIO_FROM")
        self.number_to = os.getenv("TWILIO_TO")
        self.smtp_host = os.getenv("SMTP_HOST")
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_password = os.getenv("SMTP_PASSWORD")

    def send_message(self, cheapest_flight: flight_data.FlightData):
        body_message = create_message(cheapest_flight)

        # client = Client(self.account_sid, self.auth_token)
        # message = client.messages.create(
        #     from_='whatsapp:+14155238886',
        #     body=body_message,
        #     to='whatsapp:+5519997632549'
        # )
        print(body_message)
        print(f"Number of stops: {cheapest_flight.number_stops}")

    def send_email(self, cheapest_flight: flight_data.FlightData, email_to):
        body_message = create_message(cheapest_flight)

        with smtplib.SMTP(host=self.smtp_host, port=587) as connection:
            connection.starttls()
            connection.login(user=self.smtp_user, password=self.smtp_password)
            for email in email_to["users"]:
                connection.sendmail(from_addr=self.smtp_user, to_addrs=email["email"],
                                    msg=f"Subject:Promocao de Viagem\n\nDear {email["firstName"]},\n{body_message}")
            connection.close()
