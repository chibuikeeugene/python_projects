import datetime as dt
import random
import smtplib
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

email = config['gmail.account']['email']
password = config['gmail.account']['password']


# obtain the current day
today = dt.datetime.now()

# read our quotes file
with open('./mail_automation/quotes.txt', mode='r') as file:
    data = file.readlines()

if today.weekday() == 2: # 0: Monday, 1: Tuesday ...
    selected_quote = random.choice(data)
    print(selected_quote)

    with smtplib.SMTP(host = 'smtp.gmail.com', port=587, timeout=5) as connection:
        connection.starttls()
        connection.login(
            user=email,
            password=password
        )
        connection.sendmail(msg=f'Subject: Wednesday Motivational Quote\n\n{selected_quote}', 
                            from_addr=email, to_addrs='test@gmail.com')


