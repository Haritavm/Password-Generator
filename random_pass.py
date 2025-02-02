import random
import string


def generate_password(length: int=10):
    password = []  
    for i in range(length): # Loop through the length of the password
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation)) # Generate random password
    return ''.join(password) # Convert list to string

password = generate_password(5)
print("Generated Password: ",password)