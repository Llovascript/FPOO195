#clase solicitante de nombre, apellido paterno, apellido materno, anio de nac, carrera
import string
import random


class Matricula:
    
    def __init__(self,long=3, año=2024):
        self.long = long
        self.año = año
        
        
    def generate_digits(self):
        
        characters=string.digits
        
        digitos=''.join(random.choice(characters) for _ in range(self.long) )
        return digitos
 

    