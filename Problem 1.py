import random
import string

class random_password_generator:
    def __init__(self):
        self.digits = True
        self.special_chars = False
        self.uppercase = False
        self.lowercase = True
        self.length = 8

    def set_digits(self, data):
        self.digits = data

    def set_special_chars(self, data):
        self.special_chars = data

    def set_uppercase(self, data):
        self.uppercase = data

    def set_lowercase(self, data):
        self.lowercase = data

    def set_length(self, length):
        if length <= 0:
            print(" length of password cannot be 0 or negative.")
            return
        self.length = length

    def generate_password(self):
        characters = ''
        if self.digits:
            characters += string.digits
        if self.special_chars:
            characters += string.punctuation
        if self.uppercase:
            characters += string.ascii_uppercase
        if self.lowercase:
            characters += string.ascii_lowercase


        if not characters:
            print("There should be atleast one character type")
            return None

        if self.length > len(characters):
            raise ValueError(" Password is shorter then the specified characters")

        password = random.choices(characters, k=self.length)
        return ''.join(password)

generate_pass = random_password_generator()

digits = input("Do you want to include digits? (y/n): ")
generate_pass.set_digits(digits.lower() == 'y')

special_char = input("Do you want to include special characters? (y/n): ")
generate_pass.set_special_chars(special_char.lower() == 'y')

uppercase = input("Do you want to include uppercase letters? (y/n): ")
generate_pass.set_uppercase(uppercase.lower() == 'y')

lowercase = input("Do you want to include lowercase letters? (y/n): ")
generate_pass.set_lowercase(lowercase.lower() == 'y')

length = int(input("Enter the desired password length: "))
generate_pass.set_length(length)

password = generate_pass.generate_password()
if password:
    print("Password is:", password)
