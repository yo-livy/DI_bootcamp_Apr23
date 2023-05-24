import psycopg2

# Connect to the DATABASE
connection = psycopg2.connect(
    database="RestaurantMenuManager",
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)
# Creating a cursor object
cursor = connection.cursor()
