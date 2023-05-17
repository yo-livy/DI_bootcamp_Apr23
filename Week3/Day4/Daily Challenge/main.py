# Instructions :
#
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.
#
#
#
# Part I
#
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
#
# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
#
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
import collections

text = "A good book would sometimes cost as much as a good house."
class Text:
    def __init__(self, a):
        self.a = a
        self.text_lower = self.a.lower()
        self.lst_text = self.text_lower.split()
    def freq_word(self, word):
        if word not in self.lst_text:
            return None
        else:
            return f"The word '{word}' is {self.lst_text.count(word)} times in text."

    def most_common(self):
        counter = collections.Counter(self.lst_text)
        most_common = counter.most_common()
        max_count = most_common[0][1]
        print("Most common element(s):")
        for element, count in most_common:
            if count == max_count:
               print(element)

    def unique(self):
        counter = collections.Counter(self.lst_text)
        unique_lst = []
        for key, value in counter.items():
            if value == 1:
                unique_lst.append(key)
        print(unique_lst)
        return unique_lst

# Part II
#
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
#
# Implement a classmethod that returns a Text instance but with a text file:
#
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
#
#
# Now, use the provided the_stranger.txt file and try using the class you created above.

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as file:
            text = file.read()
        return cls(text)



text1 = Text(text)
print(text1.freq_word('good'))
text1.most_common()
text1.unique()

text_from_file = Text.from_file("the_stranger.txt")
text_from_file.most_common()
freq = text_from_file.freq_word("world")
print(freq)


