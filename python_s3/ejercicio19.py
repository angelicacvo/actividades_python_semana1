import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

desired_length = 12
generated_password = generate_random_password(desired_length)
print(f"La contraseña generada es: {generated_password}")
