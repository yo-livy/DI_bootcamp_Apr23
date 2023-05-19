class AnagramChecker:
    def __init__(self, word_list_file):
        with open(word_list_file, 'r') as file:
            word_list = file.read().splitlines()
        self.word_list = word_list

    def is_valid_word(self, word):
        return word.strip().lower()

    @staticmethod
    def is_anagram(word1, word2):
        word1 = word1.lower().replace(" ", "")
        word2 = word2.lower().replace(" ", "")
        return sorted(word1) == sorted(word2)

    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []
        for i in self.word_list:
            if self.is_anagram(word, i) and word.lower() != i.lower():
                anagrams.append(i)
        return anagrams
