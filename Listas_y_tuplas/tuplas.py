#Crea un programa que llene una lista de 30 valores aleatorios en un rango del 10 al 20

import random

aleatorios=[]

for i in range(30):
    aleatorios.append(random.randrange(10,20))
    
print("numeros aleatorios:", aleatorios, end=",")

def contar_repe(lista):
    conteo = {}
    for num in lista:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1
    print("Números repetidos y sus repeticiones:")
    for num, repeticiones in conteo.items():
        print(f"{num}: {repeticiones}")
    
def eliminar_repe(lista):
    lista_sin_repetidos = list(set(lista))
    print("Lista sin repetidos:", lista_sin_repetidos)
    
def reemplazar(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                lista[j] = 0
    print("Lista con repetidos reemplazados por 0:", lista)
    

while True:
    print("MENU")
    print("1.- Contador de numeros repetidos")
    print("2.- Eliminar repetidos")
    print("3.- Reemplazar repetidos con 0")
    
    opc=input("Ingrese una opcion: ")
    
    if opc == "1":
        contar_repe(aleatorios)
    elif opc == "2":
        eliminar_repe(aleatorios)
    elif opc == "3":
        reemplazar(aleatorios)
    else:
        print("Opción inválida") 
    
    continuar = input("¿Desea terminar el programa? (Sí/No): ")
    if continuar.lower() == "si":
        print("Saliendo del programa...")
        break