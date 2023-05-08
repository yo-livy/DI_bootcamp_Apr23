# Instructions
#
# Challenge 1
#
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples
#
# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
#
# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
#
# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

number = int(input("Please, write a number: "))
length = int(input("Please, write a length: "))
answer = []
for i in range(length):
    a = number * (i + 1)
    answer.append(a)
print(answer)

# Challenge 2
#
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples
#
# user's word : "ppoeemm" ➞ "poem"
#
# user's word : "wiiiinnnnd" ➞ "wind"
#
# user's word : "ttiiitllleeee" ➞ "title"
#
# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

word = input("Please, enter a word: ")
new_word = word[0]
letter = word[0]
for i in (word[1:]):
    if i != letter:
        new_word += i
        letter = i
print(new_word)

