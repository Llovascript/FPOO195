#1.- numeros impares

num = int(input("ingresa numero: "))

for No in range(1, num):
    if No % 2!=0:
        num += No
print(','.join(1))