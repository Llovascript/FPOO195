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
            
    #deposito a otra cuenta

                
                