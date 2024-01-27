"""
#1.- Contraseña

Contra1 = str(input("ingresa tu contraseña: "))

Contra2 = str(input("Verifica tu contraseña: "))
if Contra1==Contra2:
    print("contraseña correcta")
else:
    print("contraseña incorrecta")
"""
    
"""
#2.- Par o impar
num=int(input("Ingresa un numero: "))
if num % 2 == 0:
    print("el numero", num, "es par")
else:
    print("el numero", num, "es impar")
"""

"""
#3.- Edad y costo 

edad = int(input("Edad del cliente: "))
if edad < 4:
    print("El cliente entra gratis")
elif edad >= 4 and edad <= 18:
    print("El cliente paga $110")
else:
    print("El cliente paga $190")
"""

#4.- Palindromo

palabra = input("Ingresa la palabra: ")
palindromo = palabra[::-1]
if palabra == palindromo:
    print("Es un palindromo")
else:
    print("No es un palindromo")