import string
import random

class Contraseña:

    def __init__(self, length=8, include_uppercase=False, include_special_chars=False):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_special_chars = include_special_chars

    def generate_password(self):
        characters = string.ascii_lowercase + string.digits
        if self.include_uppercase:
            characters += string.ascii_uppercase
        if self.include_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

    def check_password_strength(self, password):
        length = len(password)
        if length in range(8,11):
            return "Débil"
        elif length in range (12,15):
            return "Medio"
        else:
            return "Fuerte"
