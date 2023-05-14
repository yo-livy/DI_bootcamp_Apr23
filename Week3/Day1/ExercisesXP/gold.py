# Exercise 1 : Geometry
#
# Instructions
#
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.

import math
class Circle:
    def __init__(self, radius = 1.0):
        self.radius = radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2

    def define_circle(self):
        print("A circle is a geometrical shape consisting of all the points in a plane that are at an equal distance from a fixed point called the center of the circle.")

circle_1 = Circle(5.5)
print(circle_1.perimeter())
print(circle_1.area())
circle_1.define_circle()

# Exercise 2 : Custom List Class
#
# Instructions
#
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).

import random
class MyList:
    def __init__(self, lst_letters):
        self.lst_letters = lst_letters

    def reversed(self):
        rev_lst = self.lst_letters[::-1]
        return rev_lst

    def sorted(self):
        sort_lst = sorted(self.lst_letters)
        return sort_lst

    def rand_lst(self):
        rand_lst = [random.randint(0, 100) for letter in self.lst_letters]
        return rand_lst

lst_1 = MyList(['a','b','c','d','e','f','g','w','v','u','y','s','d','f','g'])
print(lst_1.reversed())
print(lst_1.sorted())
print(lst_1.rand_lst())

# Exercise 3 : Restaurant Menu Manager
#
# Instructions
#
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.
#
# Create a python file called menu_manager.py.
#
# Create a class called MenuManager.

menu_lst = [{'name':'Soup', 'price':10, 'spice':'B', 'gluten index': False},
            {'name':'Hamburge', 'price':15, 'spice':'A', 'gluten index': True},
            {'name':'Salad', 'price':18, 'spice':'A', 'gluten index': False},
            {'name':'French Fries', 'price':5, 'spice':'C', 'gluten index': False},
            {'name':'Beef bourguignon', 'price':25, 'spice':'B', 'gluten index': True}]
class MenuManager:
    def __init__(self, menu):
        self.menu = menu

    def print_lst(self):
        for i in self.menu:
            print(i)
    def add_item(self, name, price, spice, gluten):
        new_item = {"name":name, "price":price, "spice":spice, "gluten index":gluten}
        self.menu.append(new_item)
    def update_item(self, name, price, spice, gluten):
        item = {"name":name, "price":price, "spice":spice, "gluten index":gluten}
        for i in range(len(self.menu)):
            if item["name"] == self.menu[i]["name"]:
                self.menu[i] = item
                break
        else:
            print("There's no such dish in the menu")
    # This else statement is actually part of the for loop and is executed only if the loop completes all iterations without encountering a break statement. In other words, the else block is executed only if the desired element is not found in the list.


    def remove_item(self, name, price, spice, gluten):
        item = {"name":name, "price":price, "spice":spice, "gluten index":gluten}
        if item in self.menu:
            self.menu.remove(item)
        else:
            print("The dish is not in the menu")


my_menu = MenuManager(menu_lst)
# my_menu.print_lst()
my_menu.add_item('Onion rings', 10, 'C', True)
# my_menu.print_lst()

my_menu.update_item("Salad", 2000, "ABC", False)
my_menu.print_lst()

# my_menu.remove_item('Onion ringsss', 10, 'C', True)
# my_menu.print_lst()


# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).
#
# Here is a list of the dishes currently on the menu:
#
#     Soup – 10 – B - False
#     Hamburger – 15 - A - True
#     Salad – 18 - A - False
#     French Fries – 5 - C - False
#     Beef bourguignon– 25 - B - True
#
#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy
#
# The dishes provided above should be the value of the menu attribute.
#
# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.
#
# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.
#
# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.








