import requests as re
import os
from dotenv import load_dotenv
from twilio.rest import Client


# load environment variables
load_dotenv()

# read the api key variable
API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


LAT = 53.408371
LON = -2.991573
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'
PARAMS = {
    'lat': LAT,
    'lon': LON,
    'cnt': 5,
    'appid': API_KEY
}

# fetch weather data for my location
response = re.get(
    url=BASE_URL,
    params=PARAMS,
    timeout= 5
)

# handling http error
response.raise_for_status()

WILL_RAIN =  False

weather_ids = []

if response.status_code == 200:
    data =  response.json()

    # loop through each 3hr forecast, retrieve the weather ids and check if ids are below or equal to 600
    for forecast in data['list']:
        weather_ids.append(forecast['weather'][0]['id'])

    for value in weather_ids:
        if value <= 600:
            WILL_RAIN = True
    if WILL_RAIN:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                    body="It will rain today, bring an umbrella",
                    from_="+15017122661",
                    to="+2349083206122",
                    )

        print(message.sid)