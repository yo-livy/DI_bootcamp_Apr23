# Exercise 1 : Family
#
# Instructions
#
# Create a class called Family and implement the following attributes:
#
# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:
#
family_1 = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]
# Implement the following methods:
#
# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.

class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
    def born(self, **kwargs):
        self.members.append(kwargs)
        print("Congratulations, you have a new family member!")

    def print(self):
        print(self.members)

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name and member['age'] > 18:
                return True
        return False
    def family_presentation(self):
        print(f"{self.last_name} :")
        for member in self.members:
            print(member['name'])

family_smith = Family(family_1, "Smith")
family_smith.born(name="Sandy", age = 0, gender = 'Female', is_child = True)
family_smith.print()
print(family_smith.is_18('Sarah'))
family_smith.family_presentation()


# Exercise 2 : TheIncredibles Family
#
# Instructions
#
# Create a class called TheIncredibles. This class should inherit from the Family class:
#
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:

family_1_incred = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]
#
#
# 2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
#
#
# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.
#
#
# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.

class Incredibles(Family):
    def use_power(self):
        for member in self.members:
            if member['age'] > 18:
                print(member['power'])
            else:
                raise Exception("The member is not 18")
    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
            print(f"{member['incredible_name']} {member['power']}")


fam_inc = Incredibles(family_1_incred, "Thunder")
fam_inc.use_power()
fam_inc.incredible_presentation()
fam_inc.born(name="Baby Jack", age=0, gender="Male", is_child=True, power='Unknown Power', incredible_name = "Little Superman")
fam_inc.incredible_presentation()







