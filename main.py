# In project 9 use project 1 and apply a date time module to always tell the current year

# datetime module that imports a dates and time to the codee
from datetime import datetime

# user input for both name and age
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

# the current date and time from the datetime module
current = datetime.now().year
# calculating age and year when they will turn 100
Hundred = (current - age) + 100
print(current)
print(f"Your name is {name}, and you are currently {age} years old. You will be 100 in the year {Hundred}!")