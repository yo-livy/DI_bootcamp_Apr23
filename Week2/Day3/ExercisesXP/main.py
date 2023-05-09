# # Exercise 1 : Convert Lists Into Dictionaries
# #
# # Instructions
# #
# # Convert the two following lists, into dictionaries.
# # Hint: Use the zip method
# # keys = ['Ten', 'Twenty', 'Thirty']
# # values = [10, 20, 30]
# # Expected output:
# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#
#
keys1 = ['Ten', 'Twenty', 'Thirty']
values1 = [10, 20, 30]
my_dict1 = dict(zip(keys1, values1))
print(my_dict1)

# # Exercise 2 : Cinemax
# #
# # Instructions
# #
# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free.
# # if they are between 3 and 12, the ticket is $10.
# # if they are over the age of 12, the ticket is $15.
# #
# # Given the following object:
# #
# # family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# #
# #
# # How much does each family member have to pay ?
# #
# # Print out the family’s total cost for the movies.
# # Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
#
family = {}

while True:
    if input("Buy / Quit: ").lower() == "quit":
        break
    else:
        name = input("Please, write your name: ")
        age = input("Please, write your age: ")
        family[name] = int(age)

print(f"Family: {family}")

ticket_price = 0
total_price = 0
for key, value in family.items():
    if 3 <= value <= 12:
        ticket_price = 10
    elif value > 12:
        ticket_price = 15
    else:
        ticket_price = 0
    total_price += ticket_price
    print(f"{key} pays {ticket_price}")
print(f"Total sum for tickets: ${total_price}")


# Exercise 3: Zara
#
# Instructions
#
# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# 3. Change the number of stores to 2.

brand["number_stores"] = 2
print(brand)

# 4. Print a sentence that explains who Zara's clients are.

print("The Zara's clients are:")
for clients in brand["type_of_clothes"][:3]:
    print(clients)

# 5. Add a key called country_creation with a value of Spain.

brand["country_creation"] = "Spain"
print(brand)

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

if "international_competitors" in brand and type(brand["international_competitors"]) == list:
    brand["international_competitors"].append("Desigual")
print(brand)

# 7. Delete the information about the date of creation.

del brand["creation_date"]
print(brand)

# 8. Print the last international competitor.

print(brand["international_competitors"][-1])

# 9. Print the major clothes colors in the US.

print("The major colors in USA:")
for i in brand["major_color"]["US"]:
    print(i)

# 10. Print the amount of key value pairs (ie. length of the dictionary).

print(len(brand))

# 11. Print the keys of the dictionary.

for key in brand:
    print(key)

# 12. Create another dictionary called more_on_zara with the following details:
#
# creation_date: 1975
# number_stores: 10 000
#
#

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000,
}

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

brand.update(more_on_zara)
print(brand)

# 14. Print the value of the key number_stores. What just happened ? #We have updated the dictionary before with number_stores = 10000, that's why we reasigned the value of that key.

print(brand["number_stores"])

# Exercise 4 : Disney Characters
#
# Instructions
#
# Use this list :
#
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :
#
# #1/
#
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#
# #2/
#
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#
# #3/
#
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
#
#
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
j = 0
for i in users:
    disney_users_A[i] = j
    j += 1
print(disney_users_A)

# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.

disney_users_B = {}
j = 0
for i in users:
    disney_users_B[j] = i
    j += 1
print(disney_users_B)

# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.

disney_users_C = dict(sorted(disney_users_A.items()))
print(disney_users_C)

# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.

disney_users_A1 = {}
for i,j in disney_users_A.items():
    if "i" in i:
        disney_users_A1[i] = j
print(disney_users_A1)

# The characters, which names start with the letter “m” or “p”.

disney_users_A2 = {}
for i, j in disney_users_A.items():
    if "m" == i[0].lower() or "p" == i[0].lower():
        disney_users_A2[i] = j
print(disney_users_A2)


