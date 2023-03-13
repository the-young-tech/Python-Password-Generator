import random

characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]|/?!@#$%^abcdefghijklmnopqrstuvwxyz"
password_length = 50
password = "".join(random.sample(characters, password_length))

print("Your Generated Password: %s" %password)
