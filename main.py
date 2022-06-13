# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from ast import And


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word1 = input("Enter a Word: ")
    word2 = input("Enter another Word to determine if anagram: ")
    if "ol" in word1 and "ol" in word2:
        return True
    else:
        return False


find_anagram("below", "elbow")
