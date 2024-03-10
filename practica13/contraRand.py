import string
import random

class Contraseña:

    def __init__(self, long=8, include_uppercase=False, include_special_chars=False):
        self.long = long
        self.include_uppercase = include_uppercase
        self.include_special_chars = include_special_chars

    def generate_password(self):
        characters = string.ascii_lowercase + string.digits
        if self.include_uppercase:
            characters += string.ascii_uppercase
        if self.include_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(self.long))
        return password

    def check_password_strength(self, password):
        long = len(password)
        if long < 8:
            return "Débil"
        elif long in range (8,15):
            return "Medio"
        else:
            return "Fuerte"
