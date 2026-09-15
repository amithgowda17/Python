# A dictionary in Python is a collection of key-value pairs.
# Each key in a dictionary is associated with a value, and you can retrieve
# or manipulate data using the key. Unlike lists and tuples, dictionaries are
# unordered and mutable (changeable).

# Basic Dictionary Operations:
#
# Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
# Add a new city and its dish to the dictionary.
# Update the dish for Bengaluru.
# Remove one city from the dictionary.
# Use the keys() method to print all city names in the dictionary.
# Use the values() method to print all dishes in the dictionary.

#
# dishes={
#     "Bengaluru":"Biryani",
#     "Mysore":"Mysore Pak",
#     "Mandya":"Ragi Mudde",
# }
#
# dishes["Manglore"]="fish"
# print(dishes)
#
# dishes["Bengaluru"]="Dosa"
# print(dishes)
#
#
# dishes.pop("Manglore")
# print(dishes)
#
# print(dishes.keys())
# print(dishes.values())
# print(type(dishes.items()))

# Nested Dictionary Practice (Simple for now):

# Create a dictionary to store details of two of your friends, including their names,
# favorite subject, and favorite food.
# Access and print the favorite food of one friend.

dishes={
    "frnd1":{
        "name":"kruthik",
        "subject":"SAP",
        "food":"Biryani",
    },
    "frnd2":{
        "name":"Abhi",
        "subject":"Java",
        "food":"Mudde",
    }
}

print(dishes["frnd1"]["food"])