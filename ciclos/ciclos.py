
"""
#1.- numeros impares
num = int(input("Ingresa un numero: "))

for i in range(1, num + 1):
    if i % 2 != 0:
        print(i,end=", ")
"""

"""
#2.-cuenta regresiva
num = int(input("Ingresa tu número: "))

for i in range(num, -1, -1):
    print(i, end=", ")
"""

"""
#3.-tabla de multiplicar
num = int(input("Ingresa un número para generar la tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
"""

"""
#4.-triangulo rectangulo de cuenta regresiva
num = int(input("Ingresa Altura del Triángulo: "))
for i in range(1, num+1, 2):
    for j in range(i, 0, -2):
        print(j, end="")
    print("")
"""

"""
#5.-palabra y letra que se repite en la misma
word = input("Ingresa una palabra: ")
letter = input("Ingresa una letra: ")
count = 0
for char in word:
    if char.lower() == letter.lower():
        count += 1
print(f"La letra '{letter}' se repite {count} veces en la palabra '{word}'.")
"""


"""
#6.-Deposito y retiro de un banco y saldo final
saldo = 1000

transacciones = int(input("Número de transacciones: "))

for _ in range(transacciones):
    tipo_transaccion = input("Ingrese 'D' para depósito o 'R' para retiro: ")
    if tipo_transaccion.upper() == 'D':
        monto_deposito = float(input("Ingrese el monto a depositar: "))
        saldo += monto_deposito
    elif tipo_transaccion.upper() == 'R':
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        saldo -= monto_retiro
    else:
        print("Entrada no válida. Utilice 'D' para depósito o 'R' para retiro.")

print(f"El saldo final es: {saldo}")
"""



#7.-arbol de navidad con ciclo while
num_filas = int(input("Ingrese el número de filas del árbol de Navidad: "))
fila = 1
espacios = num_filas - 1
asteriscos = 1
while fila <= num_filas:
    for _ in range(espacios):
        print(" ", end="")
    for _ in range(asteriscos):
        print("*", end="")
    print("")
    espacios -= 1
    asteriscos += 2
    fila += 1
