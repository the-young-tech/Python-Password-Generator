import random
import string

def random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 60
password = random_password(password_length)

print("Your Generated Password: {}".format(password))