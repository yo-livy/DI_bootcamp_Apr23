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



