import os
import requests
from datetime import timedelta
from datetime import datetime as dt
from dotenv import load_dotenv


load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY =  os.getenv('ALPHA_VANTAGE_STOCK_API_KEY')

STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query?'
STOCK_BASE_URL = f'{STOCK_API_ENDPOINT}function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}'


NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_BASE_URL = 'https://newsapi.org/v2/everything'

## STEP 1: When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_DATA_EXIST =  True

while STOCK_DATA_EXIST:
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
    print(f'Yesterday\'s stock closing price: {yday_stk_price_ending}')
    day_before_yday_stk_price_ending = float(stock_data["Time Series (Daily)"][day_before_yesterday_date_str]["4. close"])
    print(f'the day before yesterday\'s closing price: {day_before_yday_stk_price_ending}')

    # compute the percentage difference
    per_diff = round((((yday_stk_price_ending - day_before_yday_stk_price_ending) / day_before_yday_stk_price_ending) * 100), 2)

## STEP 2: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    if per_diff >= 0.1 or per_diff >= -0.1: # check if the difference is greater than or equal to 5% or negative 5%
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
        print(news_list[0])


    STOCK_DATA_EXIST = False


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' 
and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' 
and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

