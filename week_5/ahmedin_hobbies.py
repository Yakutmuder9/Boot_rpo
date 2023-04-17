""" 
    Title: ahmedin_myworld.py
    Author: Professor Krasso
    Date: 16 April 2023
    Modified By: Yakut Ahmedin
    Description: Exercise 5.3 – Python Conditionals, Lists, and Loops.
"""

# list of hobbies
hobbies = ['reading', 'swimming', 'hiking', 'painting', 'cooking']

# loop to print hobbies to console
print("My hobbies:")
for hobby in hobbies:
    print("- " + hobby)

# Create a list of days
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Step 5: Use a for loop with if...else statement to display the day type
print("\nDay types:")
for day in days:
    if day == 'Saturday' or day == 'Sunday':
        print(day + ": You are off and should enjoy your hobbies!")
    else:
        print(day + ": It's a work day.")
