import os
import requests as re
from dotenv import load_dotenv
from loguru import logger
from datetime import datetime

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')

site_url = 'https://trackapi.nutritionix.com'
exercise_endpoint = '/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/27330c96272719394461fa3d6f29e6e6/myWorkout/workouts'

header = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_APP_KEY,
    'x-remote-user-id':'0'
}

query_input = input('tell us what you did today: ')


exercise_params = {
    'query':query_input,
    'weight_kg':90,
    'height_cm':160,
    'age':30
}

response =  re.post(
    url=f'{site_url}{exercise_endpoint}',
    json=exercise_params,
    headers=header,
    timeout=10
)

if response.status_code == 200:
    logger.info(response.json())
    # get the current date and time
    datetime_value = datetime.now()
    str_date = datetime_value.strftime("%d/%m/%Y, %H:%M:%S")
    date = str_date[:10]
    time = str_date[-8:]

    # get the post body paramenters
    data =  response.json()
    exercise = data['exercises'][0]['name']
    duration = data['exercises'][0]['duration_min']
    calories = data['exercises'][0]['nf_calories']

    # post body request
    workout_param = {
        'workout': {
            'date':date,
            'time':time,
            'exercise':exercise,
            'duration':duration,
            'calories':calories,
        }
    }

    # call the post method to send data to our google sheet using sheet endpoint
    try:
        response = re.post(
            url=sheety_endpoint,
            json=workout_param,
            timeout=10
        )

        logger.success(response.text)
    except Exception as e:
        logger.error(f"Couldn't submit request due to {e}")