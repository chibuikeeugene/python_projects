import requests
from datetime import datetime
import smtplib
import random
import configparser
import time

config = configparser.ConfigParser()

config.read('config.ini')

email = config['gmail.account']['email']
password = config['gmail.account']['password']

MY_LAT = 53.410580
MY_LONG = -2.977940


# check if the iss is overhead
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

# check when it is dark
def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout= 10)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now <= sunrise or time_now >= sunset:
        return True

#run the code every 60 seconds.
while True:
    time.sleep(60)
    #If the ISS is close to my current position
    # and it is currently dark

    if is_iss_overhead() and is_dark():

        # access email by creating a connection
        with smtplib.SMTP(host = 'smtp.gmail.com', port=587, timeout=5) as connection:
            connection.starttls()
            connection.login(
                user=email,
                password=password
            )

            # Then send me an email to tell me to look up.
            connection.sendmail(msg='Subject: Wednesday Motivational Quote\n\nLook up to the sky',
                                from_addr=email, to_addrs='test@gmail.com')





