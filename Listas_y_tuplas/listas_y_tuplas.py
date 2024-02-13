#Crea un programa usando funciones y lo que necesites para que el usuario inserte N números en una Tupla, después de la captura debe desplegar el siguiente menú funcional
from statistics import mode
def ing_num():
    N=int(input("Ingresa numeros en la tupla"))
    tupla = tuple(int(input(f"Ingrese el número {i + 1}: ")) for i in range(N))
    return tupla
    
def suma(tupla):
    return sum(tupla)
def mayor(tupla):
    return max(tupla)
def menor(tupla):
    return min(tupla)
def promedio(tupla):
    return sum(tupla)/float(len(tupla))
def moda(tupla):
    return mode(tupla)
def rango(tupla):
    return max(tupla)-min(tupla)
            
tupla=ing_num()

while True:
    print("MENU")
    print("1.- Sumatoria de los elementos")
    print("2.- Numero mayor")
    print("3.- Numero menor")
    print("4.- Promedio")
    print("5.- MODA")
    print("6.- Rango")
    
    opc=input("Ingrese una opcion: ")
    
    if opc=="1":
        print("la suma de numeros es:", suma(tupla))
    elif opc=="2":
        print("El mayor de la tupla es:", mayor(tupla))  
    elif opc=="3":
        print("El menor de la tupla es:", menor(tupla))
    elif opc=="4":
        print("El promedio de la tupla es:", promedio(tupla))
    elif opc == "5":
        print("La moda de la tupla es:", moda(tupla))
    elif opc == "6":
        print("El rango de la tupla es:", rango(tupla))
    else:
        print("opcion invalida") 
        break

    continuar = input("¿Desea terminar el programa? (Sí/No): ")
    if continuar.lower() == "si":
        print("Saliendo del programa...")
        break