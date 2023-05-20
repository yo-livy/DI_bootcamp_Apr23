# Instructions :
#
# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

import requests
import time

list_of_websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

def response_time(list):
    for url in list:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        delta = end_time - start_time
        print(f"It takes {delta} seconds a webpage - {url} - to load.")

response_time(list_of_websites)
