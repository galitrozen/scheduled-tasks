import smtplib
import datetime as dt
import pandas as pd
import random
import os


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
now = dt.datetime.now()
today= (now.month, now.day)

data = pd.read_csv("birthdays.csv") #pandas DataFrame
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

print(birthday_dict)
if today in birthday_dict:
    print("great")
    BD_person = birthday_dict[today]
    letter_path = f"letter_{random.randint(1,3)}.txt"
    with open(letter_path) as file:
        content = file.read()
        content = content.replace("[NAME]",BD_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs= BD_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n {content}" )
