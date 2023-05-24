import requests
import pprint
import random

def get_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error occurred while retrieving data from the API.")
        return None
data = get_data_from_api('https://restcountries.com/v3.1/all')
# pprint.pprint(data[4])
# pprint.pprint(data[0]['name']['common'])
# pprint.pprint(data[0]['capital'][0])
# pprint.pprint(data[0]['flag'])
# pprint.pprint(data[0]['subregion'])
# pprint.pprint(data[0]['population'])

random_10_countries = []
country = []
for i in range(10):
    num = random.randint(0,100)
    country = [data[num]['name']['common'], data[num]['capital'][0], data[num]['flag'], data[num]['subregion'], data[num]['population']]
    random_10_countries.append(country)
# pprint.pprint(random_10_countries)

import psycopg2

# Connect to the DATABASE
connection = psycopg2.connect(
    database="Countries_10",
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)
# Creating a cursor object
cursor = connection.cursor()


