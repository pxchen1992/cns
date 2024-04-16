# healthcheck.py

import requests
import datetime
import time

def check_time_service(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            current_time = response.text.strip()
            server_time = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
            current_local_time = datetime.datetime.now()
            time_diff = abs((current_local_time - server_time).total_seconds())
            if time_diff <= 1:
                print("Time service is up and clock is synchronized.")
            else:
                print("Time service is up but clock is desynchronized by more than 1 second.")
        else:
            print("Failed to fetch time from service.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    service_url = "http://<service_ip>:80/now" # Replace <service_ip> with the IP of pod service
    while True:
        check_time_service(service_url)
        time.sleep(60) # Check every minute
