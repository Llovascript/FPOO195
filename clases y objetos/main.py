from Personaje import *
from armas import *


#solicitar datos Spartan
print("====Datos de Heroe====")
nombreS=input("Escribe el nombre de tu Spartan: ")
especieS=input("Escribe la especie de tu Spartan: ")
alturaS=float(input("Escribe la altura de tu Spartan: "))

#solicitar datos Nemesis
print("====Datos de Villano====")
nombreN=input("Escribe el nombre de tu Nemesis: ")
especieN=input("Escribe la especie de tu Nemesis: ")
alturaN=float(input("Escribe la altura de tu Nemesis: "))

#creamos el obj de la clase personaje
Spartan = Personaje(especieS,nombreS,alturaS)
Nemesis = Personaje(especieN,nombreN,alturaN)
arma=armas()

print("====El obj Spartan contine====")
print(Spartan.nombre)
print(Spartan.especie)
print(Spartan.altura)        
print("")

print("====El obj Villano contine====")
print(Nemesis.nombre)
print(Nemesis.especie)
print(Nemesis.altura) 
print("")

#usamos los metodos del spartan
print("====Metodos del obj Spartan====")
Spartan.correr(True)
Spartan.lanzarGranada()
print("")

print("====Metodos del obj Nemesis====")
Nemesis.correr(True)
Nemesis.lanzarGranada()
print("")

#usamos metodos del arma
arma.seleccionarArma(Spartan.nombre)
arma.recargarArma(65)