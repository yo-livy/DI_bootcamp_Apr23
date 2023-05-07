# Exercise 3 : Outputs
#
# Instructions
#
# Predict the output of the following code snippets:
#     >>> 3 <= 3 < 9 True
#     >>> 3 == 3 == 3 True
#     >>> bool(0) False
#     >>> bool(5 == "5") False
#     >>> bool(4 == 4) == bool("4" == "4") True
#     >>> bool(bool(None)) False
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
#
#     print("x is", x) True
#     print("y is", y) False
#     print("a:", a) 5
#     print("b:", b) 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Exercise 4 : How Many Characters In A Sentence ?
#
# Instructions
#
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
           Ut enim ad minim veniam, quis nostrud exercitation ullamco
           laboris nisi ut aliquip ex ea commodo consequat.
           Duis aute irure dolor in reprehenderit in voluptate velit
           esse cillum dolore eu fugiat nulla pariatur.
           Excepteur sint occaecat cupidatat non proident,
           sunt in culpa qui officia deserunt mollit anim id est laborum."""

my_text_variable = len(my_text)
print(my_text_variable)

# Exercise 5: Longest Word Without A Specific Character
#
# Instructions
#
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

sentence = ''
max_sentence = ''
i = 0
while sentence.find("A") == -1:
    sentence = input("Maybe you know more the longest sentence without A: ")
    if len(sentence) > len(max_sentence) and sentence.find("A") == -1:
        max_sentence = sentence
        print("Congrats, keep on doing")
        i += 1
    elif len(sentence) <= len(max_sentence) and sentence.find("A") == -1:
        print("Try again, the sentence is not longer than the previous one")

print("Sorry, you are lost, your points are", i)

