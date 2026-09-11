# A list is a collection of items that are ordered, mutable (changeable),
# and allow duplicate elements. Lists can hold items of different data types,
# such as integers, strings, or even other lists.

# List Manipulation Exercise:
#
# Create a list of items (strings or numbers or any).
# Add a new item to the end of the list and another at the second position.
# Remove the third item from the list.
# Print the list after each operation.

grocery_items=["idli batter","chicken","mutton",False,7]
grocery_items.append("ragi")# Add a new item to the end of the list
print(grocery_items)

grocery_items.insert(1,"fish") #another at the second position.
print(grocery_items)

grocery_items.pop(2)
print(grocery_items)

# Reverse and Sort a List: Create a list of numbers and:
#
# Sort it in descending order.
# Reverse the sorted list and print it.

numbers=[2,5,6,1,4,2]
numbers.sort() #they return nothing , no return type
print(numbers)
numbers.reverse() #they return nothing , no return type
print(numbers)

# or

# numbers.sort(reverse=True)
# print(numbers)


# You cannot directly sort mixed strings and numbers
# items = ["apple", 10, "banana", 5]
# items.sort()
#
# This gives a TypeError because Python cannot directly compare a string with an integer.
#
# But strings that contain numbers can be sorted
#
# If the numbers are stored as strings, it works:
#
# items = ["apple", "10", "banana", "5"]
#
# items.sort()
# print(items)
#
# Output:
#
# ['10', '5', 'apple', 'banana']
#
# Notice that "10" comes before "5" because Python is sorting them as strings, not numbers.
#
# If you want actual numeric sorting
# numbers = ["10", "5", "20", "2"]
#
# numbers.sort(key=int)
# print(numbers)
#
# Output:
#
# ['2', '5', '10', '20']
#
# So:
#
# [10, 5, 20, 2] → numeric sorting
# ["10", "5", "20", "2"] → string/alphabetical sorting
# ["apple", 10, "banana", 5] → direct sorting
# ["apple", "10", "banana", "5"] → sorting