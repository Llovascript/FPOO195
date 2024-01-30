"""

palabra = input("ingresa una palabra: ")
cont_voc=0
for letra in palabra:
    if letra.lower() in "aeiou":
        cont_voc += 1
        
print(f"la palabra'{palabra}' tiene {cont_voc} vocal(es)." )
"""

#suma de numeros pares del 1 al 10

suma = 0
for num in range(1,11):
    if num % 2==0:
        suma += num
print(f"la suma de los numeros es: {suma}")
    