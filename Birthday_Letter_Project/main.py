##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import smtplib
from random import randint

MYEMAIL = "YOUR_EMAIL"
MYPASSWORD = "YOUR_PASSWORD"

birthdays = pd.read_csv("birthdays.csv")
birthdays = birthdays.to_dict(orient="records")

today = dt.datetime.today()


for row in birthdays:
    if row["month"] == today.month and row["day"] == today.day:
        filename = f'letter_templates/letter_{randint(1, 3)}.txt'
        with open(file=filename) as file:
            text = file.read()
            text = text.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MYEMAIL, password=MYPASSWORD)
            connection.sendmail(from_addr=MYEMAIL, to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday :D\n\n{text}")
            connection.close()

        print(f"Email send to {row["name"]} - {row["email"]}")

