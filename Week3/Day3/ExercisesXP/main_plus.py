# Exercise 2: Random Module
#
# Instructions
#
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

import random
def random_number():
    num = int(input("Input a number from 1 to 100: "))
    if num in range(101):
        num_1 = random.randint(1, 100)
        if num == num_1:
            print("Success!!!")
        else:
            print(num)
            print(num_1)
            print("The numbers are not equal")
    else:
        print("Out of range")

# random_number()

# Exercise 3: String Module
#
# Instructions
#
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import string

def string_length():
    str = string.ascii_letters
    return ''.join(random.choice(str) for i in range(5))
print(string_length())


# Exercise 4 : Current Date
#
# Instructions
#
# Create a function that displays the current date.
# Hint : Use the datetime module.

import datetime
def date_func():
    print(datetime.date.today())

date_func()

# Exercise 5 : Amount Of Time Left Until January 1st
#
# Instructions
#
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

def time_to_1():
    return  datetime.date(2024,1,1) - datetime.date.today()
print(f"Time left till 1st of January 2024: {time_to_1()}")

# Exercise 6 : Birthday And Minutes
#
# Instructions
#
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

def how_many_minutes(birthday):
    date_format = "%Y-%m-%d"
    date_obj = datetime.datetime.strptime(birthday, date_format)
    delta = datetime.datetime.today() - date_obj
    return int(delta.total_seconds()/60)
print(f"Minutes: {how_many_minutes('1985-7-3')}")

# Exercise 7 : Upcoming Holiday
#
# Instructions
#
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.
import math
def today_date():
    holiday_date = "2023-5-26"
    holiday_date_formated = datetime.datetime.strptime(holiday_date,"%Y-%m-%d")
    today = datetime.datetime.today()
    time_until_holidays = holiday_date_formated - today
    days = time_until_holidays.days
    hours, remainder = divmod(time_until_holidays.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return(f"Today is {today.strftime('%Y-%m-%h')}. The next holiday is in {days} days {hours}:{minutes}:{seconds} hours")

print(today_date())

# Exercise 8 : How Old Are You On Jupiter?
#
# Instructions
#
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

def how_old(seconds):
    earth = seconds / 31557600
    other_planet = {
        'Earth' : earth,
        'Mercury' : 0.2408467,
        'Venus' : 0.61519726,
        'Mars' : 1.8808158,
        'Jupiter' : 11.862615,
        'Saturn' : 29.447498,
        'Uranus' : 84.016846,
        'Neptune' : 164.79132
    }
    for key, value in other_planet.items():
        print(f"{key}: {value * earth} earth years")
how_old(1000000000)

# Exercise 9 : Faker Module
#
# Instructions
#
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

from faker import Faker

fake = Faker()
users = []

def create_user():
    user = {
        'name':fake.name(),
        'address':fake.address(),
        'language_code':fake.language_code()
    }
    return user
for i in range(10):
    users.append(create_user())
for i in users:
    print(i)













