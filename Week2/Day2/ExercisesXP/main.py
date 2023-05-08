#  Exercise 1 : Set
#
# Instructions
#
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {1, 2, 3, 4, 5, 6, 7, 8}
my_fav_numbers.add(9)
my_fav_numbers.add(10)
print(my_fav_numbers)

mfn_list = list(my_fav_numbers)
mfn_list.pop()
mfn_new_set = set(mfn_list)
print(mfn_new_set)

friend_fav_numbers = {10, 20, 30 ,40 ,50}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2: Tuple
#
# Instructions
#
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# No, we can't add more integers to the tuple, because tuples are immutable, their elemets cannot be modified once created. Althoug, we can concatenate two tupils in new one. And we can use unpacking(*) of one of the tuple to create a new one: new = (*tuple, 1, 2, 3, 4)

# Exercise 3: List
#
# Instructions
#
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)

basket.pop()
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0, "Apples")
print(basket)

apple_count = basket.count("Apples")
print(apple_count)

basket.clear()
print(basket)

# Exercise 4: Floats
#
# Instructions
#
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

my_list = []
for i in range(3, 11):
    i /= 2
    if i.is_integer():
        i = int(i)
    my_list.append(i)
print(my_list)

# Exercise 5: For Loop
#
# Instructions
#
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for i in range(1, 21):
    print(i)

my_list = list(range(1, 21))
i = 0
for num in my_list:
    if i % 2 == 0:
        print(my_list[i])
    i += 1

# Exercise 6 : While Loop
#
# Instructions
#
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

name = 'Eugene'
ask = ''
while ask.lower() != name.lower():
    ask = input("What's your name? : ")

# Exercise 7: Favorite Fruits
#
# Instructions
#
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fav_fruit = input("Please, write your favourite fruits, separate by space: ")
list_fruit = fav_fruit.split()
any_fruit = input("Write any fruit: ")
if any_fruit in list_fruit:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")

# Exercise 8: Who Ordered A Pizza ?
#
# Instructions
#
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

topping_list = []
while True:
    ask_toppings = input("Add toppings or quit: ")
    if ask_toppings == 'quit':
        break
    else:
        topping_list.append((ask_toppings))
        print(f"You will add {ask_toppings} to your pizza")
print("Your pizza will be with:")
for i in topping_list:
    print(i)
total_price = 10 + len(topping_list)*2.5
print(f"Total price is {total_price} $.")

# Exercise 9: Cinemax
#
# Instructions
#
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Ask a family the age of each person who wants a ticket.
#
# Store the total cost of all the family’s tickets and print it out.
#
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

age = input("Write your family ages, separate by space: ")
age_list = age.split()
ticket_price = 0
total = 0
for i in range(len(age_list)):
    age_list[i] = int(age_list[i])
    if age_list[i] > 12:
      ticket_price = 15
      total += ticket_price
    elif 3 <= age_list[i] <= 12:
      ticket_price = 10
      total += ticket_price
print(f"Total price is {total}")

name_list = ['Adam', 'Mary', 'Tony', 'Clara']
approved_list = []
for name in name_list:
    age_cinema = input(f"Hi, {name}! How old are you?  ")
    if int(age_cinema) < 16 or int(age_cinema) > 21:
        approved_list.append(name)
print(approved_list)

# Exercise 10 : Sandwich Orders
#
# Instructions
#
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
#
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

finished_sandwiches = []
for i in sandwich_orders:
    finished_sandwiches.append(i)
    print(f"I have made your {i}")
# Exercise 11 : Sandwich Orders#2
#
# Instructions
#
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders.extend(["Pastrami sandwich", "Pastrami sandwich"])
print(sandwich_orders)

print("The deli has run out of pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
new_finished_sandwiches = []
for i in sandwich_orders:
    new_finished_sandwiches.append(i)
    print(f"I have made your {i}")
