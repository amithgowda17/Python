# A set is a collection of unique items that is unordered and unindexed.
# Sets do not allow duplicate values. Sets are useful for performing operations
# like union, intersection, and difference.
from list import grocery_items

# Set Operations:
#
# Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
# Find the union, intersection, and difference between the two sets.
# Add a new fruit to your set.
# Remove a fruit from your set using both remove() and discard().
# What happens when the fruit doesn’t exist?

favorite_fruits={"apple","pomegranate","watermelon","strawberry"}
friend_favorite_fruits={"watermelon","strawberry","orange"}

favorite_fruits.add("dragon fruit")
print(favorite_fruits)

# favorite_fruits.remove("a") if exits will remove , if not will through error
print(favorite_fruits)


favorite_fruits.discard("apple") # if not exists , it will just discard the function6
print(favorite_fruits)

# Tuple and Set Comparison:
#
# Create a list of elements and convert it into both a tuple and a set.
# Print both the tuple and the set.
# Try to add new elements to the tuple and set. What differences do you observe?

grocery_item=["ragi","egg","chilli"]
converted_set=set(grocery_item)
print(converted_set)

converted_tuple=tuple(grocery_item)
print(converted_tuple)