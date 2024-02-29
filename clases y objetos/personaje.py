class Personaje:
    
    #atributo de personaje
    #declaramos el constructor para crear los obj
    def __init__(self, esp, nom, alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    
        #metodos del personaje
    def correr(self, __estado):
        if (__estado):
            print("el personaje "+self.__nombre+ "esta corriendo")
        else:
            print("el personaje "+self.__nombre+ " esta muerto")
 
    def lanzarGranada(self):
        print(self.__nombre+" pego una granada")
    
    #getters    
    def get__especie(self):
        return self.__especie
    
    
    def get__nombre(self):
        return self.__nombre
    
    def get__altura(self):
        return self.__altura
    
    #setters
    def set__especie(self, __especie):
        self.__especie = __especie
         
    def set__nombre(self, __nombre):
        self.__nombre = __nombre
        
    def set__altura(self, __altura):
        self.__altura = __altura
    

            
