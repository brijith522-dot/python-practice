#BMI Calculator
name = input("Enter your name: ")                       #getting user input
age = int(input("Enter your age: "))                    #getting user input 
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))
height = height / 100                                   #height conversion from cm to m
if height <= 0 or weight <= 0:                          #input validation
    print("Height and weight must be greater than zero.")
    exit()
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
    print("Consult a healthcare professional if needed and focus on a nutritious diet.")
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    print("You have a healthy weight for your height.")
    category = "Normal weight"   
elif 25 <= bmi < 29.9:
    print("Consider adopting a healthier lifestyle with a balanced diet and regular exercise.")
    category = "Overweight"
elif bmi >= 30:
    print("Consult a healthcare professional for a comprehensive weight management plan.")
    category = "Obese"
    print("Category:", category)

print("============================")
