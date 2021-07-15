# Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

# (You may assume that the input to add_dots does not itself contain any dots.)

# create a new variable that is a string to add the chars and dots to
# String = ""
#  Iterate over the length of the string -----> for i in string
# for the index, return the index and value, so do enumerate, to be able to keep the value of the index
# After each index, add a comma, except the last one, GO TO BASICS with concantenate after each index, except the last one
# need to rejoin the char into a string, with the commas .join()


def  add_dots(word):
    string = ""
    for i, char in enumerate(word):
        if i < len(word) - 1:
            string += char+"."
        else:
            string += char
    else:
        return string

# print(add_dots("test"))


def  remove_dots(word):
    string = ""
    for i, char in enumerate(word):
        if char != ".":
            string += char            
    else:
        return string

print(remove_dots(add_dots("test")))