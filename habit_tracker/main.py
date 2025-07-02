import requests as re
from loguru import logger
from datetime import datetime
from random import randint

USERNAME = "chuby"
TOKEN = "tradavad65adhad8aianda"
GRAPH_ID = "graph1"

pixela_new_user_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f'{pixela_new_user_endpoint}/{USERNAME}/graphs'


headers = {
    'X-USER-TOKEN': TOKEN
}


user_params = {
    "token": TOKEN,
    "username": USERNAME, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes",
}

graph_config = {
    "id":"graph1",
    "name":"Coding-graph",
    "unit":"secs",
    "type":"int",
    "color":"shibafu"
}

# create user account
# first check if the user already exists 
user_exists = re.get(url=f'https://pixe.la/@{USERNAME}', timeout=10)
if user_exists.status_code != 200:

    response  =  re.post(url= pixela_new_user_endpoint, json=user_params, timeout= 10)
    logger.info(response.text)

# creating a graph with our user account
graph_exists = re.get(url=f'{graph_endpoint}/{GRAPH_ID}/stats', timeout= 10)
if graph_exists.status_code != 200:

    response = re.post(url=graph_endpoint, headers=headers, json=graph_config, timeout= 10)
    logger.info(response.text)

# post a new pixel using your new account to the remote graph
posting_pixel_graph_endpoint = f'{graph_endpoint}/{GRAPH_ID}'
pixel_config = {
    "date":str(datetime.now().date()).replace('-', ''),"quantity":str(randint(60, 120))
}

response =  re.post(url=posting_pixel_graph_endpoint, json=pixel_config, headers=headers, timeout=10)
logger.info(response.text)
