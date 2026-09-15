# A function is a reusable block of code that performs a task when called.
#
# Function parameters and arguments
#
# A parameter is a variable in the function definition. An argument is the value
# passed when calling the function.
#
# Positional arguments : Values are assigned to parameters according to their order.
#
# show("Anand", 21)
#
# Keyword arguments : Values are assigned using parameter names, so their order can vary.
#
# show(age=21, name="Anand")
#
# Default parameter values :A parameter uses its default value when no argument is provided for it.
#
# def greet(name="Student"):
#

# Greet Function: Write a function greet() that takes no arguments and prints a greeting message.
def greet():
    print("Hello Namaskara !!!!!!")

greet()

# Parameterized Greet: Write a function greet_user() that takes a name as input
# and prints a custom greeting.

def greet_user(name):
    print(f"hello {name} namaskara !!!!!!")

greet_user("Ravi")

# Sum Function: Write a function add_numbers(a, b) that returns the sum of two numbers.
# Call this function with different values.

def add_numbers(a, b):
    return a + b

print(add_numbers(1, 2))
print(add_numbers(0, 8))
