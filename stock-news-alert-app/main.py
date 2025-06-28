import os
import requests
from datetime import timedelta
from datetime import datetime as dt
from dotenv import load_dotenv
from twilio.rest import Client
from loguru import logger


load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY =  os.getenv('ALPHA_VANTAGE_STOCK_API_KEY')

STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_BASE_URL = f'{STOCK_API_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}'


NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_BASE_URL = 'https://newsapi.org/v2/everything'

# obtain the respective dates and save them as variables
today_date = dt.now().date()

yesterday_date_str = str(today_date - timedelta(days=1))

day_before_yesterday_date_str = str(today_date - timedelta(days=4)) # set to 2 later

# fetch stock data
response =  requests.get(
    url = STOCK_BASE_URL,
    timeout = 5
)

response.raise_for_status()

stock_data =  response.json()

# print(stock_data)

# obtain the stock closing value for each date
yday_stk_price_ending  = float(stock_data["Time Series (Daily)"][yesterday_date_str]["4. close"])
logger.info(f'Yesterday\'s stock closing price: {yday_stk_price_ending}')

day_before_yday_stk_price_ending = float(stock_data["Time Series (Daily)"][day_before_yesterday_date_str]["4. close"])
logger.info(f'the day before yesterday\'s closing price: {day_before_yday_stk_price_ending}')

# compute the percentage difference
diff = round(yday_stk_price_ending - day_before_yday_stk_price_ending, 2)
per_diff = round((( abs(diff) / day_before_yday_stk_price_ending) * 100), 2)
logger.info(f'diff: {diff}, per_diff: {per_diff}')

# the up_down arrow logic
up_down = None
if diff > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

if per_diff > 0.1: # check if the percentage diff is greater than 0.1

    # get the first 3 trending news about the organization
    NEWS_PARAM = {
        'q':'tesla',
        'from': str(day_before_yesterday_date_str),
        'sortBy':'publishedAt',
        'apiKey': NEWS_API_KEY
    }

    news_response = requests.get(
        url=NEWS_BASE_URL,
        params=NEWS_PARAM,
        timeout= 5
    )

    news_list =  [] # a list object to hold all news data

    news_data = news_response.json()

    # retrieve the first three recent news of the company
    news_items = news_data['articles'][:3]


    for news_item in news_items:
        news_list.append({'title': news_item['title'], 'descritpion': news_item['description']})
    logger.info(f'{news_list[0]}')


    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    # loop through each article message 
    for news_data in news_list:
        message_body =  f"""
    TSLA: {up_down}{per_diff}%
    Headline: {news_data['title']}?. 
    Brief: {news_data['descritpion']}
    """
        message = client.messages.create(
            body=message_body,
            from_='+15139825653',
            to= '+18777804236'
        )