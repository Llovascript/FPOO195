#escribir un programa que visualice en pantalla los numeros multiplos de 10 complendidos entre 10 y 1000

num = int(input("Desde qué número deseas los múltiplos hasta el mil: "))

for i in range(num, 1001, 10):
    print(i,end=", ")

