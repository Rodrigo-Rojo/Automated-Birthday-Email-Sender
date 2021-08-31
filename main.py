import pandas
import random
import smtplib
import datetime as dt
try:
    birthdays_data = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    data_dict = {
        "name": ["Randy", "Armando", "Merilyn"],
        "email": ["test@gmail.com", "test@gmail.com", "test@yahoo.com"],
        "year": ["1995", "1994", "1992"],
        "month": ["1", "2", "3"],
        "day": ["4", "5", "6"]
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("birthdays.csv", index=False)
finally:
    birthdays_data = pandas.read_csv("birthdays.csv")

random_letter = random.choice(["letter_templates/letter_1.txt", "letter_templates/letter_2.txt",
                               "letter_templates/letter_3.txt"])
email = "test@gmail.com"
password = "test12345"
today_formatted = dt.datetime.today().strftime("%Y-%m-%d")
year = dt.datetime.today().year

for person in birthdays_data.to_dict(orient="records"):
    birthday = dt.date(year, person["month"], person["day"])
    if str(birthday) == str(today_formatted):
        print("it is your birthday")
        with open(random_letter) as starting_letter:
            letter = starting_letter.read()
            fix_letter = letter.replace("[NAME]", person["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(
                    from_addr=email,
                    to_addrs=person["email"],
                    msg=f"Subject: Happy Birthday {person['name']}\n\n{fix_letter}"
                )
