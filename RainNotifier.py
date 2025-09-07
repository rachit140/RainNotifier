#Created by Rachit
#On 08-09-2025

import requests
from twilio.rest import Client
import time

api_key = "" #Enter your API key here
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

long = 0.0  # Enter your longitude here, 
lat = 0.0   # Enter your latitude here,
cnt = 4

account_sid = "" #Enter your account SID here
auth_token = "" #Enter your auth token here


weather_params = {
    "lat": lat,
    "lon": long,
    "cnt": cnt,
    "appid": api_key
}
# https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=fabe7bd041f714c888c1611434b7edb1

# https://api.openweathermap.org/data/2.5/forecast?lat=77.706413&lon=28.984463&appid=fabe7bd041f714c888c1611434b7edb1

def check_weather():
    response = requests.get(OWM_Endpoint, params=weather_params)
    response.raise_for_status()

    weather_data = response.json()

    print(weather_data["list"][0]["weather"][0]["id"])

    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:", #Enter your Twilio WhatsApp number here
            body="It's going to rain soon. Remember to bring an '☔️,👕'",
            to="whatsapp:" #Enter your phone number here
        )

        print(message.status)
    else:
        print("No rain expected in the next few hours.")

while True:
    check_weather()

    time.sleep(10800)
