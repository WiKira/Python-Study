# import smtplib
#
# my_email = "william.ccgo@gmail.com"
# my_password = "tdiwjoltibbeliei"
#
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
#
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email, to_addrs="william.cgo@hotmail.com",
#                     msg="Subject:Hello\n\nThis is a body message.")
# connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# if year == 2024:
#     print("Wear a face mask, you are ugly")
# print(year)
#
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1996, month=10, day=20)
# print(date_of_birth)

import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
if now.weekday() == 0:

    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()

    motivacional_phase = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="YOUR EMAIL", password="YOUR APP PASSWORD")
        connection.sendmail(from_addr="YOUR EMAIL", to_addrs="ANOTHER EMAIL",
                            msg=f"Subject:Motivacional\n\n{motivacional_phase}")
        connection.close()
