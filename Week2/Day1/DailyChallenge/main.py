# Instructions
#
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
#
# Then, print the first and last characters of the given text.
#
# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World
#
#
# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
#
# Hlrolelwod

string = input("Please, write 10 chars string: ")
if len(string) < 10:
    print("String is not long enough.")
elif len(string) > 10:
    print("String is too long.")
else:
    print("It's fine, the string is wright length.")

print(string[0], string[-1])

new_string = ''
for i in string:
    new_string += i
    print(new_string)

import random

string_list = list(string)
random.shuffle(string_list)
jumbled_string = ''.join(string_list)
print(jumbled_string)
