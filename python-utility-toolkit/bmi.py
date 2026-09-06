#BMI Calculator
name = input("Enter your name: ")                       #getting user input
age = int(input("Enter your age: "))                    #getting user input 
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)                            #BMI calculation

print("============================")                   #output generation
print("BMI Report")
print("============================")

print("Name:", name)
print("Age:", age, "Years")
print("Height:", height, "m")
print("Weight:", weight, "kg")
print("BMI:", round(bmi, 2))

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"  
elif 25 <= bmi < 29.9:
    category = "Overweight"
elif bmi >= 30:
    category = "Obese"
print("Category:", category)

print("============================")