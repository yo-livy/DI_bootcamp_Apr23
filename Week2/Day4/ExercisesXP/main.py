# Exercise 1 : What Are You Learning ?
#
# Instructions
#
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    print("Hi, I'm learning on this course!")

display_message()

#  Exercise 2: What’s Your Favorite Book ?
#
# Instructions
#
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favotire_book(title):
    print(f"One of my favorite books is {title}")

favotire_book("The Odyssey")

# Exercise 3 : Some Geography
#
# Instructions
#
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country="Ireland"):
    print(f"{city} is in {country}")

describe_city("Paris", "France")

# Exercise 4 : Random
#
# Instructions
#
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random
def func(num):
    if num in range(1, 101):
        num1 = random.randint(1, 100)
        if num == num1:
            print("Success!")
        else:
            print("Fail", num, num1)
    else:
        print("You need to input a number from 1 to 100")
func(5)

# Exercise 5 : Let’s Create Some Personalized Shirts !
#
# Instructions
#
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().
#
# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.
#
# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size="L", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")
make_shirt("L", "Batman")
make_shirt("L")
make_shirt("M")
make_shirt("XL", "Superman")
make_shirt(text="Hello World!", size="XXL")

# Exercise 6 : Magicians …
#
# Instructions
#
# Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for i in magician_names:
        print(i)
show_magicians()

def make_great():
    for i in range(len(magician_names)):
        magician_names[i] += " the Great"
        print(magician_names[i])

make_great()
show_magicians()



# Exercise 7 : Temperature Advice
#
# Instructions
#
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
#
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
#
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
#
# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().
#
# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
#
import random
def get_random_temp(season):
    if season == "winter":
        temp = random.randint(-10, 16)
    else:
        temp = random.randint(17, 40)
    return float(temp)

print(get_random_temp("Autumn"))

def main():
    month = int(input("Please, write a month (1-12): "))
    if month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    elif month in [9, 10, 11]:
        season = "autumn"
    else:
        season = "winter"
    rand_temp = get_random_temp(season)
    print(f"The temperature right now is {rand_temp} degrees Celsius.")
    if rand_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif rand_temp <= 16:
        print("Quite chilly! Don’t forget your coat")
    elif rand_temp <= 23:
        print("It's quite nice weather! But not hot!")
    elif rand_temp <= 32:
        print("It's time to go on a beach!")
    else:
        print("It's really hot! Stay at shadow and drink water!")

main()












