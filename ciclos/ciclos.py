#1.- numeros impares

num = int(input("ingresa numero: "))
odd_numbers = []

for i in range(1, num + 1):
    if i % 2 != 0:
        odd_numbers.append(str(i))

print(",".join(odd_numbers))