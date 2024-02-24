class armas:
    
    def seleccionarArma(self, nombre):
        seleccion=int(input("Seleccionar el arma:\n 1=Rifle de asalto\n 2=Espada de energia\n 3=Rifle M392"))
        if(seleccion==1):
            print("Rifle de asalto asignado a "+ nombre)
            print("Municiones 7.62*52mm, sin mira")
            
        if(seleccion==2):
            print("Espada de energia asignada a "+ nombre)
            print("Arma creada por los Shangheili")
            
        if(seleccion==3):
            print("Rifle M392 asignada a "+ nombre)
            print("Municiones 7.62*52mm, sin mira")
    
    def recargarArma(self, municion):
        cargador=25
        cargador=cargador+municion
        print("arma recargada "+str(cargador)+"%")