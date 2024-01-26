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

#4.-contador de letras

nombre = input("Ingresa tu nombre: ")

nombre_mayu = nombre.upper()
numero_letras = len(nombre_mayu)

print("Nombre en mayúsculas:", nombre_mayu," Número de letras:", numero_letras)