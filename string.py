# Simple Greeting Program: Write a Python program that asks the user for
# their name and age, then prints a personalized greeting message.
# Use both the + operator and f-strings for output.
#
# Example:
#
# Enter your name: Alice
# Enter your age: 25
# Output: Hello, Alice! You are 25 years old.
name=input("Enter your name:")
age=input("Enter your age:")

print("Hello,"+" "+name+"!"+ " "+"You are "+age+" years old.")

print(f"Hello, {name}! You are {age} years old.")

# String Manipulation Exercise: Write a Python program that:
#
# Takes a sentence as input from the user.
# Prints the sentence in all uppercase and lowercase.
# Replaces all spaces with underscores.
# Removes leading and trailing whitespace.
# Example:
#
# Input: "   Python is awesome!   "
# Output:
# Uppercase: "PYTHON IS AWESOME!"
# Lowercase: "python is awesome!"
# Replaced: "___Python_is_awesome!___"
# Stripped: "Python is awesome!"

word=input("Add your input:")
print(word.upper())
print(word.lower())
print(word.replace(" ","_"))
print(word.replace("_"," "))
print(word.strip())

# Character Counter: Write a Python program that:
#
# Asks the user for a string.
# Prints how many characters are in the string, excluding spaces.
# Example:
#
# Input: "Hello World"
# Output: "Number of characters (excluding spaces): 10"

word=input("add a word:")
print(f"Number of characters (excluding spaces): {len(word.replace(" ",""))}")

# Escape Sequence Practice: Write a Python program that uses escape
# sequences to print the following output:
#
# Example:
#
# Hello
#     World
# This is a backslash: \

print(f"Hello \n \t World \n This is a backslash: \\")