import string
import random

characters = string.ascii_letters + string.digits + string.punctuation

password = ""
cont = ""

while True:
    length = int(input("Enter the Length of the Password : "))
    if length<8 :
        print("Password must be at least 8 characters long.")
        choice=input("Do you want to generate another password(y/n) : ")
        if choice.lower() == "n":
            break
        elif choice.lower() == "y" :
            continue
    else :
        for i in range(length) :
            password += random.choice(characters)
        print(f"Generated Password : {password}")
        choice=input("Do you want to generate another password(y/n) : ")
        if choice.lower() == "n":
            break
        elif choice.lower() == "y":
            continue