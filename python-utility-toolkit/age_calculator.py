#Age Calculator
from  datetime import date
current_year =date.today().year
birth_year= int(input("Enter the year of birth: ")) #getting user input
if birth_year > current_year:                       #validating birth year
    print("You have entered an invalid year of birth, instead of that please enter a valid year of birth.")
else:
    age = current_year - birth_year                 #Age calculation
    if age>120:
        print("Please enter a realistic birth year")
    else:
        months=age * 12
        days=age * 365


    print("===========================")            #output generation
    print("AGE REPORT")
    print("========================")
    print("Birth year:", birth_year)
    print("Current year:",current_year)
    print("Age:",age,"Years")
    print("Months:",months)
    print("Days:",days)
    if age in range(0, 12):
        status = "Child"
    elif age in range(13, 17):
        status = "Teenager"
    elif age in range(18,59):
        status = "Adult"
    elif age in range(60, 120):
        status = "Senior Citizen"
    print("Status:",status)
    print("===========================")