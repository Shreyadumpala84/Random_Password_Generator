import random
import string
try:
    length = int(input("Enter Password length: "))
    if length <= 0:
        print("Please enter a valid password length")
    else:
        characters= (string.ascii_letters + string.digits + string.punctuation)
        password =""
        for i in range(length):
            password += random.choice(characters)
        print("Generated Password:", password)
except ValueError:
    print("Please enter numbers only")
