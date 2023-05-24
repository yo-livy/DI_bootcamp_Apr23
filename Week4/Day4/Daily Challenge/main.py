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
# pprint.pprint(data[0])
# pprint.pprint(data[0]['name']['common'])
# pprint.pprint(data[0]['capital'][0])
# pprint.pprint(data[0]['flag'])
# pprint.pprint(data[0]['subregion'])
# pprint.pprint(data[0]['population'])

random_10_countries = []
country = []
for i in range(10):
    num = random.randint(0, 100)
    name = data[num].get('name', {}).get('common', 'N/A')
    capital = data[num].get('capital', ['N/A'])[0]
    flag = data[num].get('flag', 'N/A')
    subregion = data[num].get('subregion', 'N/A')
    population = data[num].get('population', 'N/A')

    country = [name, capital, flag, subregion, population]
    random_10_countries.append(country)
pprint.pprint(random_10_countries)

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

for i in random_10_countries:
    save_to_table = f"""
    INSERT INTO countries (name, capital, flag, subregion, population)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(save_to_table, i)

connection.commit()
cursor.close()
connection.close()
