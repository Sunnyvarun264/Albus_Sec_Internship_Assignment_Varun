# Q.5 Write a Python script to generate strong passwords of a specified length, including a mix of uppercase letters, lowercase letters, numbers, and special characters.

import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Example usage
length = 12
password = generate_password(length)
print("Generated Password:", password)
