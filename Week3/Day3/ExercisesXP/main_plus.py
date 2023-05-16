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

random_number()

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










