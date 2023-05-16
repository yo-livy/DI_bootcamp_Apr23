# Exercise 1 : Built-In Functions
#
# Instructions
#
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.
#
# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

def func():
    class Num:
        """
        This is the documentation of the class
        """
        def __init__(self, value):
            self.value = value

        def __abs__(self):
            return abs(self.value)

        def __int__(self):
            return int(self.value)

    number = Num(-7.4)
    print(number.__abs__())
    print(number.__int__())
    print(number.__doc__)

func()


# Exercise 2: Currencies
#
# Instructions
#
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
#     #Your code starts HERE
    def __str__(self):
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"
    def __repr__(self):
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"
    def __int__(self):
        return int(self.amount)
    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            else:
                return self.amount + other.amount
        else:
            return self.amount + int(other)

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            else:
                self.amount += other.amount
                return self
        else:
            self.amount += int(other)
            return self

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'
print(str(c1))

# >>> int(c1)
# 5
print(int(c1))

# >>> repr(c1)
# '5 dollars'
print(repr(c1))

# >>> c1 + 5
# 10
print(c1 + 5)

# >>> c1 + c2
# 15
print(c1 + c2)

# >>> c1
# 5 dollars
print(c1)

# >>> c1 += 5
# >>> c1
# 10 dollars
c1 += 5
print(c1)

# >>> c1 += c2
# >>> c1
# 20 dollars
c1 += c2
print(c1)

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
c1 + c3