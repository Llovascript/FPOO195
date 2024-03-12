#clase solicitante de nombre, apellido paterno, apellido materno, anio de nac, carrera
#generador de matricula
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
 

    def datos(self):
        self.nac = input("Año de Nacimiento: ")
        self.nombre = input("Nombre: ")
        self.apellidoP = input("Apellido paterno")
        self.apellidoM = input("Apellido materno")
        self.Carrera= input("Nombre de carrera")


    