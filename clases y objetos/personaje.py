class Personaje:
    
    #atributo de personaje
    #declaramos el constructor para crear los obj
    def __init__(self, esp, nom, alt):
        self.especie = esp
        self.nombre = nom
        self.altura = alt
        
    
    #metodos del personaje
    def correr(self, estado):
        if (estado):
            print("el personaje "+self.nombre+ "esta corriendo")
        else:
            print("el personaje "+self.nombre+ " esta muerto")
            
    def lanzarGranada(self):
        print(self.nombre+" pego una granada")