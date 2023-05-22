from anagram_checker import AnagramChecker

def main():
    choice = input("Please, input a (w)ord or (e)xit: ").lower()
    while choice != 'e':
        # choice = input("Please, input a (w)ord or (e)xit: ").lower()
        # if choice == "e":
        #     print("Bye, bye!")
        #     break
        if choice == "w":
            check_word()
            choice = input("Please, input a (w)ord or (e)xit: ").lower()
            # continue
        elif choice != "w":
            print("The input is incorrect.")

def check_word():
    word = input("Please, input a single word: ")
    anagrams = AnagramChecker("sowpods.txt")
    word = word.strip().lower()
    try:
        if " " in word:
            raise ValueError("It's not a single word.")
        for i in word:
            if not i.isalpha():
                raise TypeError("It's should be a word of letters.")
    except ValueError as error:
        print(error)
    except TypeError as error1:
        print(error1)
    lst_of_anagrams = anagrams.get_anagrams(word)
    lst_of_anagrams_str = ', '.join(lst_of_anagrams).lower()
    print(f"YOUR WORD :'{word.title()}'")
    if anagrams.is_valid_word(word):
        print(f"This is a valid English word.\nAnagrams for your word: {lst_of_anagrams_str}.")
    else:
        print("This is an invalid English word.")

main()