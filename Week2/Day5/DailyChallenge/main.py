# Instructions
#
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:
#
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

def sequence_com(word):
    original_list = word.split(',')
    sorted_list = sorted(original_list) #or we can use original_list.sort()
    new_word = ','.join(sorted_list)
    print (new_word)
sequence_com("without,hello,bag,world")