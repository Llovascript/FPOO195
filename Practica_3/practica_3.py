#1.- Calcular salario\
"""
horas = float(input("Ingrese el número de horas trabajadas: "))
coste= float(input("Ingrese el coste por hora: "))

paga = horas * coste

print("La paga del usuario es:", paga, "pesos")


#.2 nombre completo
nom=str(input("Ingresa tu nombre: "))

nom_minu = nom.lower()
nom_mayu = nom.upper()
nom_mix = nom.title()

print("Nombre completo en minúsculas:", nom_minu)
print("Nombre completo en mayúsculas:", nom_mayu)
print("Nombre completo con solo la primera letra en mayúscula:", nom_mix)
"""
"""
#3.- suma de los enteros
num=int(input("ingresa el numero: "))
sum=0

for i in range(1, num+1):
    sum=sum+i
    print(sum)
"""

"""
#4.-contador de letras

nombre = input("Ingresa tu nombre: ")

nombre_mayu = nombre.upper()
numero_letras = len(nombre_mayu)

print("Nombre en mayúsculas:", nombre_mayu," Número de letras:", numero_letras)
"""

"""
#5.-peso total del paquete

num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_munecas = int(input("Ingrese el número de muñecas vendidas: "))

peso_payaso = 112
peso_muneca = 75

peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)

print("El peso total del paquete es:", peso_total, "gramos")
"""


#6.- frase invertida

palabra = input("Ingresa una palabra: ")

palabra_invertida = palabra[::-1]

print("La palabra invertida es:", palabra_invertida)