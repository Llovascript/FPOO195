#Crea un programa usando funciones y lo que necesites para que el usuario inserte N números en una Tupla, después de la captura debe desplegar el siguiente menú funcional
from statistics import mode, multimode

N=int(input("Ingresa numeros en la tupla: "))
tupla = tuple(int(input(f"Ingrese el número {i + 1}: ")) for i in range(N))

def suma():
    return sum(tupla)
def mayor():
    return max(tupla)
def menor():
    return min(tupla)
def promedio():
    return sum(tupla)/float(len(tupla))
def moda():
    
             


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
        print("la suma de numeros es:", suma())
    elif opc=="2":
        print("El mayor de la tupla es:", mayor())  
    elif opc=="3":
        print("El menor de la tupla es:", menor())
    elif opc=="4":
        print("El promedio de la tupla es:", promedio())
 
    else:
        print("opcion invalida") 

