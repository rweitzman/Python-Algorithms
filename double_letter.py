# Double letters
# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

# separate individudal letters into elements into new var w/ .list() = ["", "", ""]
# Do I need to check to see if the elements are letters? What if the string has letters and numbers? 
# ---> if yes, type() if == int push to newList = []:
#  ---> newList.push
# ---> work on just that [] with the following code:
# check to see if any consecutive match:
# if two consecutive match, 
# if list.length == list.length - 1
# return true
# else 
# return false 

def double_letters(word):
    n = len(word)
    for i in range(n - 1) :
        if(word[i] == word[i + 1]):
            return True
    else:
        return False

print(double_letters("lall"))

