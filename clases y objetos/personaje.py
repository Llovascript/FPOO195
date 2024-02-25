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