# Exercise 1 : Hello World-I Love Python
#
# Instructions
#
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

print("Hello world\n" * 4 + "I love python\n" * 4)

# Exercise 2 : What Is The Season ?
#
# Instructions
#
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month = int(input("Please input a month (1 to 12): "))
if 3 <= month <= 5:
    print("It's a Spring")
elif 6 <= month <= 8:
    print("It's a Summer")
elif 9 <= month <= 11:
    print("It's a Autumn")
else:
    print("It's a Winter")
