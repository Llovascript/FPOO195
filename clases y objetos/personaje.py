class Personaje:
    
    #atributo de personaje
    especie="Humano"
    nombre="John"
    altura= 2.18
    
    #metodos del personaje
    def correr(self, estado):
        if (estado):
            print("el personaje"+self.nombre+ "esta corriendo")
        else:
            print("el personaje"+self.nombre+ " esta muerto")
            
    def lanzarGranada(self):
        print(self.nombre+" pego una granada")
        
    def recargarArma(self, municion):
        cargador=25
        cargador=cargador+municion
        print("arma recargada"+str(cargador)+"%")

#creamos el obj de la clase personaje
Spartan= Personaje()

print(Spartan.nombre)
print(Spartan.especie)
print(Spartan.altura)        