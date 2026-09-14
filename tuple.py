# A tuple is a collection of items that is ordered and immutable (unchangeable).
# Tuples are similar to lists, but once a tuple is created, you cannot modify it.
# They are often used to group related data together.
#
# Syntax:
# my_tuple = (element1, element2, element3, ...)

# Tuple Operations:
#
# Create a tuple with 5 elements.
# Try to modify one of the elements. What happens?
# Perform slicing on the tuple to extract the second and third elements.
# Concatenate the tuple with another tuple.

my_checkList=(91,"java","python",True,"Spring")

# print(my_checkList.index("python"))
# print(my_checkList.count("python")) #check how many this exists

print(my_checkList[1:3])

second_checkList=(2,"fast api")

concatenated=my_checkList+second_checkList
print(concatenated)