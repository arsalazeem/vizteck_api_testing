import init_chrome
import datetime
import time
import requests
import pdb
from datetime import date
import json





def checkk_loading_Time(url):
    driver = init_chrome.start()
    time.sleep(7)
    intial_seconds = int(datetime.datetime.now().strftime("%S"))
    intial_minutes = int(datetime.datetime.now().strftime("%M"))
    driver.get(url)
    final_seconds = abs(int(datetime.datetime.now().strftime("%S")))
    final_minutes = int(datetime.datetime.now().strftime("%M"))
    total_time = str(final_minutes - intial_minutes) + " Minute" + " " + str(
        (final_seconds - intial_seconds)) + " " + "Seconds"
    print(total_time)
    response = requests.get(url)
    statuscode = str(response.status_code)
    if statuscode == "200":
        messege = "Site is Up"
        print(messege)
    print(statuscode)

checkk_loading_Time("https://nesma.ondemandstartup.com/")
