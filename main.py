import requests
import smtplib
import random

EMAIL = your_email_here
PASSWORD = your_app_password_here

LOTR_ENDPOINT = "https://the-one-api.dev/v2"
API_KEY = your_api_key
my_header = {"Authorization": "Bearer " + API_KEY,}


def get_character(id):
    '''takes character_id from api and returns character name'''
    endpoint = f"{LOTR_ENDPOINT}/character/{id}"
    response = requests.get(url=endpoint, headers=my_header)
    response.raise_for_status()

    return response.json()["docs"][0]["name"]

def get_quote():
    '''returns random quote from lotr api'''
    endpoint = f"{LOTR_ENDPOINT}/quote"
    response = requests.get(url=endpoint, headers=my_header)
    response.raise_for_status()
    data = response.json()["docs"]

    chosen_quote = random.choice(data)

    character = get_character(chosen_quote['character'])
    quote = random.choice(data)["dialog"]

    return f"{quote}\n\n-{character}"


message = get_quote()
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs=any_email_you_want,
                        msg=f"Subject: Daily Quote from Middle Earth\n\n{message}")
