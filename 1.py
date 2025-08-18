#To create a password generator #
import random
import string

def generate_Password(length):
    if length <8:
        print("Password length should be atlest 8.")
        return None

    all_charecters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(all_charecters)for _ in range(length))
    return password

length=int(input("Enter the password length: "))
password=generate_Password(length)
if password:
    print(f"Generated password: {password}")