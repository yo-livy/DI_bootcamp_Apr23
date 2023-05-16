# Instructions :
#
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
#
# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them
import math
import turtle

class Circle:

    def __init__(self, radius = None, diameter = None):
        self.radius = float(radius)
        self.diameter = float(diameter)
        self.name = "Circle_Radius_" + str(self.radius)

    def __str__(self):
        return self.name

    @classmethod
    def from_radius(cls, radius):
        '''Calculate the diameter getting the radius as arg'''
        return cls(radius=radius, diameter=radius * 2)

    @classmethod
    def from_diameter(cls, diameter):
        '''Calculate the radius getting the diameter as arg'''
        return cls(diameter=diameter, radius=diameter / 2) #?need more explanation?

    def draw(self):
        turtle.bgcolor("yellow")
        turtle.pencolor("green")
        turtle.pensize(30)
        turtle.circle(self.radius)

    def get_area(self):
        return math.pi * self.radius ** 2

    def __add__(self, other):
        return self.get_area() + other.get_area()

    def __gt__(self, other):
        if self.get_area() > other.get_area():
            return f"{self} is greater than {other}"
        else:
            return f"{other} is greater than {self}"

    def compare_equal(self, other):
        if self.get_area() == other.get_area:
            return "Circles are equal"
        else:
            return "Circles are not equal"

    def list_and_sort(self, *args):
        lst_circle = [self]
        for i in args:
            lst_circle.append(i)
        lst_circle.sort()
        return lst_circle

circleA = Circle.from_radius(radius=100)
circleB = Circle.from_diameter(diameter=300)
circleC = Circle(70, 140)
print(circleA)
circleA.draw()
circleB.draw()
circleC.draw()
print(circleA > circleB)
print(f"The total area of {circleA} and {circleB} is", round(circleA + circleB, 2))
print(circleA.compare_equal(circleB))
for i in (circleA.list_and_sort(circleB, circleC)):
    print(i) #?why i can't print not in for loop?



