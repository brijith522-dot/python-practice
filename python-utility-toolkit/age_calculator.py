#Age Calculator
yearofbirth = int(input("Enter the year of birth: "))
currentyear = int(input("Enter the current year: "))
if yearofbirth > 2026:
    print("You have entered an invalid year of birth, instead of that please enter a valid year of birth.")
else:
    age = currentyear - yearofbirth
    months=age * 12
    days=age * 365
    print("Your age is", age,"years.")
    print("Approximately", months,"months.")
    print("Approximately", days,"days.")