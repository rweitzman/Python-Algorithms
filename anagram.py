# Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

# take each argument and order each one sorted()
# check length, is not same length, exit
# if lengths are the same, compare the indices to check value if same (method?)

# my_string = "ROBIN"
# print(sorted(my_string))

def is_anagram(word1, word2):
    word1_1=sorted(word1)
    word2_2=sorted(word2)
    if len(word1_1) != len(word2_2):
        return False

    for i in range(len(word1_1)):
        if word1_1[i] != word2_2[i]:
            return False
    else:
        return True

print(is_anagram("robin", "nibor"))

