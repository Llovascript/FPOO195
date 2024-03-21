class Cta:
    # constr de la lista
    def __init__(self):
        self.__lista=[]
        
    # metodos de la cuenta(CRUD)
    #cada cuenta tiene registrados los siguientes datos: No. Cuenta, titular, edad y saldo
    def Alta(self,NoCta,Titular,edad,saldo):
        saldo=float(saldo)
        self.__lista.append({"No. Cuenta: ":NoCta, "Titular:":Titular, "Edad: ":edad, "Saldo: ": saldo})
        
    # Consultar saldo
    def ConsultaSaldo(self, NoCta, Titular):
        for cuenta in self.__lista:
            if cuenta["No. Cuenta: "] == NoCta and cuenta["Titular:"] == Titular:
                return cuenta['Saldo: ']
        return None
        
    #retirar efectivo
    def retiro(self, NoCta, Titular, cantidad):
        for cuenta in self.__lista:
            if cuenta["No. Cuenta: "] == NoCta and cuenta["Titular:"] == Titular:
                saldoini = cuenta['Saldo: ']
                if saldoini >= cantidad:
                    cuenta['Saldo: '] -= cantidad
                    return cuenta['Saldo: ']
                else:
                    return "saldo insuficiente para retirar"
        return "titular o numero de cuenta inexistente"
    #def deposito(self, NoCta, Titular, cantidad):
        #for cuenta in self.__lista:
           # if cuenta["No. Cuenta: "] == NoCta and cuenta["Titular:"] == Titular:
               # cuenta['Saldo: '] += cantidad
               # return cuenta['Saldo: ']
            
    #transferencia a otra cuenta
    def transferencia(self, NoCta_origen, Titular_origen, NoCta_destino, Titular_destino, cantidad):
        saldo_origen = self.ConsultaSaldo(NoCta_origen, Titular_origen)
        saldo_destino = self.ConsultaSaldo(NoCta_destino, Titular_destino) 
        if saldo_origen is not None and saldo_destino is not None:
            if saldo_origen >= cantidad:
                for cuenta in self.__lista:
                    if cuenta["No. Cuenta: "] == NoCta_origen and cuenta["Titular:"] == Titular_origen:
                        cuenta['Saldo: '] -= cantidad
                    elif cuenta["No. Cuenta: "] == NoCta_destino and cuenta["Titular:"] == Titular_destino:  
                        cuenta['Saldo: '] += cantidad
                return True, "Transferencia exitosa"
            else:
                return False, "Saldo insuficiente en la cuenta de origen"
        else:
            return False, "No se encontraron una o ambas cuentas"


        

                
                