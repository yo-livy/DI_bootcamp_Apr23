class Anargamchecker:
    def __init__(self, text_file):
        self.text_file = text_file

    def is_valid_word(self, word):
        pass

    def get_anagrams(self, word):
        pass

    @classmethod
    def is_anagram(cls, word1, word2):
        word1 = word1.lowercase().replace(" ", "")
        word2 = word2.lowercase().raplace(" ", "")

        if len(word1) != len(word2)
            return False

        count1 = {}
        count2 = {}
        # Count the occurrences of each letter in word1
        for letter in word1:
            count1[letter] = count1.get(letter, 0 ) + 1 #.get(p , 0) method retrieves a value associated with its parameter. Return ) if there is no parameter

        # Count the occurrences of each letter in word2
        for letter in word2:
            count2[letter] = count2.get(letter, 0) + 1

        # Compare the dictionaries
        return count1 == count2

