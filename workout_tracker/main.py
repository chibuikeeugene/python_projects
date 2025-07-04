import os
import requests as re
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')

site_url = 'https://trackapi.nutritionix.com'
exercise_endpoint = '/v2/natural/exercise'

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
    print(response.json())