# Basic Conditions:
#
# Write a program to check if someone is eligible for a bus pass. If they are below 5 years,
# the bus pass is free. If they are 60 years or older, they get a senior citizen discount.
# Otherwise, they pay the full price.

age=int(input("Enter your age to check eligibility: "))
if age<5:
    print("the fare will be free for you..")
elif age>=60:
    print("Based on your age you will get senior citizen discount")
else:
    print("You will come under normal fare charges")

# Meal Time Checker:
# Create a program that checks the time of day (24-hour format) and prints whether it's
# time for breakfast, lunch, or dinner.
# Breakfast: 8 AM
# Lunch: 1 PM
# Dinner: 8 PM
# If none of these times, print "It's not meal time."

time=input("enter the current time to meal time in am or pm : ").strip()

if time.upper()=="8 AM":
    print("its break fast time")
elif time.upper()=="1 PM":
    print("its lunch time")
elif time.upper()=="8 PM":
    print("its dinner time")
else:
    print("it's not meal time")

