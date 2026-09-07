#Password Generator
import random
import string
password = ""
Length=int(input("Enter the length of the password: "))  #getting user input
if Length<=0:
    print("Password length must be greater than zero.")

Numbers=input("Include number's? (yes/no): ").lower()
Symbols=input("Include special characters? (yes/no): ").lower()
Uppercase=input("Include uppercase letters? (yes/no): ").lower()
if Length<0:
    print("Password length must be greater than zero.")

characters = string.ascii_lowercase  #default characters to lowercase letters

if Numbers == "yes":
    characters += string.digits
if Symbols == "yes":
    characters += string.punctuation
if Uppercase == "yes":
    characters += string.ascii_uppercase
for i in range(Length):
    password += random.choice(characters)  #generating password

print("Generated Password:", password)
if Length <8:
    print("Strength: Weak")
elif length<12:
    print("Strength: Moderate")
else:
    print("Strength: Strong")
    



