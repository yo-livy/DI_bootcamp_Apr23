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





