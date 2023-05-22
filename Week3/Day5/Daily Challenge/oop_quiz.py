# Part 1 : Quizz :

# Answer the following questions

# What is a class?
# A class is a blueprint or a template that defines the attributes (data) and behaviors (methods) of objects. It is used to create objects with similar properties and functionalities.
# What is an instance?
# An instance, also known as an object, is a specific occurrence or realization of a class. It represents a unique entity with its own set of data and behavior based on the defined class.
# What is encapsulation?
# Encapsulation is a principle of object-oriented programming that bundles the data and related methods within a class, hiding the internal details and providing a public interface for interacting with the object. It ensures data integrity and enhances modularity and code reusability.
# What is abstraction?
# Abstraction is a concept that focuses on representing essential features and behavior while hiding unnecessary details. It allows us to create abstract classes or interfaces that define common properties and methods, providing a generalized view of objects.
# What is inheritance?
# Inheritance is a mechanism in object-oriented programming where a class inherits the properties and methods of another class. It allows the derived class (subclass) to reuse and extend the functionality of the base class (superclass), promoting code reuse and hierarchical relationships.
# What is multiple inheritance?
# Multiple inheritance refers to a feature in some programming languages where a class can inherit properties and methods from more than one base class. It allows a class to inherit characteristics from multiple parent classes, potentially resulting in complex relationships and potential conflicts.
# What is polymorphism?
# Polymorphism is the ability of objects to take on different forms or have multiple behaviors based on their context. It allows objects of different classes to be treated as objects of a common superclass, enabling code flexibility and extensibility.
# What is method resolution order or MRO?
# Method Resolution Order (MRO) defines the sequence in which the methods of a class hierarchy are invoked when there are inheritance and overriding involved. It determines which implementation of a method will be used in case of method name conflicts between classes in the inheritance hierarchy.




# Part 2: Create A Deck Of Cards Class.
#
# The Deck of cards class should NOT inherit from a Card class.
#
# The requirements are as follows:
#
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random

class Card:
    def __init__(self, suit, value):
         self.suit = suit
         self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"
class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []
        self.generate_deck()
    def generate_deck(self):
        for i in self.suits:
            for j in self.values:
                card = Card(i, j)
                self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

deck = Deck()
deck.generate_deck()
for i in deck.cards:
    print(i)
deck.shuffle()
print("_________")
print("_________")
print("_________")
for i in deck.cards:
    print(i)
print("_________")
print("_________")
print("_________")
print(deck.deal())
