# Exercise 1 : Pets
#
# Instructions
#
# Using this code:
#
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
#
# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

class Siamese(Cat):
    pass

cat_bengal = Bengal("Bunny", 3)
cat_chart = Chartreux("Bugs", 1)
cat_sia = Siamese("Ricky", 2)

all_cats = [cat_bengal, cat_chart, cat_sia]

sara_pets = Pets(all_cats)
sara_pets.walk()

# Exercise 2 : Dogs
#
# Instructions
#
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
#
# Create 3 dogs and run them through your class.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print (f"{self.name} is barking")
    def run_speed(self):
        return (self.weight/self.age)*10
    def fight(self, other_dog):
        winner = None
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            winner = self.name
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            winner = other_dog.name
        else:
            print("It's a tie!")
        print(f"The winner is {winner}!")
dog_1 = Dog("Rock", 5, 50)
dog_2 = Dog("Terminator", 4, 70)
dog_3 = Dog("Pinky", 2, 5)


dog_1.bark()
dog_2.bark()
dog_3.bark()

print(dog_1.run_speed())
print(dog_2.run_speed())
print(dog_3.run_speed())

dog_1.fight(dog_2)
dog_1.fight(dog_3)
dog_2.fight(dog_3)

# Exercise 3 : Dogs Domesticated
#
# Instructions
#
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
#
# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.
#
# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        self.bark()
        self.trained = True
    def play(self, *other_dogs):
        dog_names = []
        for i in other_dogs:
            dog_names.append(i.name)
        print(f"{', '.join(dog_names)} all play together")
    def do_a_trick(self):
        if self.trained == True:
            import random
            random_number = random.randint(1, 4)
            if random_number == 1:
                print(f"{self.name} does a barrel rock")
            elif random_number == 2:
                print(f"{self.name} stands on his back legs")
            elif random_number == 3:
                print(f"{self.name} shakes your hand")
            else:
                print(f"{self.name} plays dead")
        else:
            print("The dog is not trained!")

dog_4 = PetDog("Stormy", 3, 35)
dog_4.train()
dog_4.play(dog_3, dog_1, dog_2)
dog_4.do_a_trick()

