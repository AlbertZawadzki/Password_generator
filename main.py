import random
import string

def password():
    while True:
        strength = input("How stron password do you want? w/m/s")
        match strength:
            case "w":
                return ''.join(random.choice(string.ascii_letters) for _ in range(length))
                break
            case "m":
                return ''.join(random.choice(string.ascii_letters + string.ascii_letters) for _ in range(length))
                break
            case "s":
                return ''.join(random.choice(string.ascii_letters + string.ascii_letters + string.punctuation) for _ in range(length))
                break

question = input("Do you want to generate password? y/n")

if question=="y":
    while True:
        try:
            length = int(input("How long password do you want to receive?"))
            print(password())
            answer = input("Is this password satisfied? y/n")
            if answer=="y":
                break
        except ValueError:
            print("Please enter a number")


