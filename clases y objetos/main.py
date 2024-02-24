from Personaje import *
from armas import *

#creamos el obj de la clase personaje
Spartan = Personaje()
arma=armas()

print(Spartan.nombre)
print(Spartan.especie)
print(Spartan.altura)        

#usamos los metodos del spartan
Spartan.correr(True)
Spartan.lanzarGranada()

#usamos metodos del arma
arma.seleccionarArma(Spartan.nombre)
arma.recargarArma(65)