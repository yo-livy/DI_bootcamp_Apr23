# Exercise 1 : Hello World
#
# Instructions
#
# Print the following output in one line of code:
#
# Hello world
# Hello world
# Hello world
# Hello world

print('Hello\n' * 4)

# Exercise 2 : Some Math
#
# Instructions
#
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

print((99 ** 3) * 8)

# Exercise 3 : What Is The Output ?
#
# Instructions
#
# Predict the output of the following code snippets:
# >>> 5 < 3 False
# >>> 3 == 3 True
# >>> 3 == "3" False
# >>> "3" > 3 TypeError
# >>> "Hello" == "hello" False

# Exercise 4 : Your Computer Brand
#
# Instructions
#
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = "Apple"
print(f"I have a {computer_brand} computer")

# Exercise 5 : Your Information
#
# Instructions
#
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = "Eugene"
age = 37
shoe_size = 44
info = f"Interseting sentence about {name} who is {age} years old and have shoe size of {shoe_size}."
print(info)

# Exercise 6 : A & B
#
# Instructions
#
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger than b, have your code print Hello World.

a = 8
b = 5
if a > b:
    print("Hello world")
print("b is greater than a")

# Exercise 7 : Odd Or Even
#
# Instructions
#
# Write code that asks the user for a number and determines whether this number is odd or even.

ask = input("Input number: ")
if int(ask) % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Exercise 8 : What’s Your Name ?
#
# Instructions
#
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

my_name = "Eugene"
ask_name = input("Hi! What's your name: ")
if ask_name.lower() == my_name.lower():
    print("Wow, we both have one name)")
else:
    print("It's ok that we have different names)")

# Exercise 9 : Tall Enough To Ride A Roller Coaster
#
# Instructions
#
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

user_height = int(input("Hi! What's your height? : "))
if user_height * 2.54 > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")
