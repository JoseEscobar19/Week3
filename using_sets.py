# number_set = {1,2,3,4,4} duplicate values are removed
#output is just {1,2,3,4}

# you cant use mutable data types inside a set, such as lists, dictionaries
number_set = {1,2,3,4, [5, 6]}
print(number_set)

# we will try this again, but using a tuple, because a tuple is immutable
number_set = {1,2,3,4, (5,6)} #tuples are immutable data type, so theyre okay to use in a set
print(number_set)

'''
set items cant be accesed by an index because set are not ordered, and do not have keys.
but they can be iterated though, allowing to access it items
'''
# the output is a mix of the words in one sentence, theyre different each time because sets are unordered, 
words_set = {"alpha", "bravo", "charlie"}
abcd = ""

for word in words_set:
    abcd += word
print(abcd)

# If we just need to check if there is an item in a set
# we can use the "in" keywrord for this - which will return either boolean true or false

if "alpha" in words_set:
    print("alpha is in set")
else:
    print("Alpha not in set")

#modifying set values 
#since sets are mutables that means we an add item inside as long as theyreimmutables
"""
to add an item, its the .add("") method, ex: variable.addMethod("example")
to remove an item its the .discard method: variable.discard("name of the item")
"""

words_set.add("delta")
print(words_set)

words_set.discard("bravoo")
print(words_set)
