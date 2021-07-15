# Counting syllables
# Define a function named count that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

# "ho-tel"
# "cat"
# "met-a-phor"
# "ter-min-a-tor"
# Your function should count the number of syllables and return it.

# For example, the call count("ho-tel") should return 2.

# take in word
# make word into a list -----> list
# look for non-letter items isalpha ----> isalpha seems best, but it won't work on a list and returns false since there ARE non-alphas in the word
# what about making a list and then using order? but then I would need to iterate and I still can't use type, so I would run into the same issues. there HAS to be a solution, so it is a method I don't know?
# add non-character items to a syls[] append
# len of syls[]
# len of new array + 1 = syllables
# return syllables


# I wanted to do type check but the types are int, float, list, dic, tuple, does not include letter/num/symbol
# I tried to turn the string into a list so i could check each char indidivually to see if they are letters, and i cant use isalpha on a list, what can I use on a list? i'd like to append all char that are - to syls in a for loop and then add 1 and return and then print that value. 

# def count(word):
#     syls=[]
#     for ele in word:
#         if word.isalpha():
#             print("True")
#         else:
#             print("False")
    # syllables = len(syls) + 1
    # return syllables
# print(count("hotel"))

# s = "ho-tel"
# for char in s: print(char, char.isalpha())


# def count(word):
#     # sysl = []
#     for char in word:
#         return(char, char.isalpha())
#     # sysl.append(return(char, char.isalpha())

# print(count("ho-tel"))

# def count(word):
#     syllables = 1
#     for char in word:
#         if char.isalpha() == False:
#            syllables += 1 
#     else:
#         return syllables

# print(count("ho-tel"))

def count(word):
    syllables = 1
    for char in word:
        if char == "-":
           syllables += 1 
    else:
        return syllables

print(count("ho-tel"))