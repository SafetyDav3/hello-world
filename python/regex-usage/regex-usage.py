# A program that takes user input and validates it using regex


import re


def is_valid_email(email):
    pattern = r"^[\w]+[\w.+-]*@[\w]+\.[a-zA-Z]+$"
    return bool(re.match(pattern, email))


if __name__ == "__main__":
    while True:
        email = input("Enter an email address: ")
        if is_valid_email(email):
            print(f"{email} is a valid email address.")
        else:
            print(f"{email} is not a valid email address.")
