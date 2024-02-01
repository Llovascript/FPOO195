#1.- area de un circulo y volumen del cilindro
import math

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_cilindro(altura, area_base):
    return altura * area_base

def main():
    radio_circulo = float(input("Ingrese el radio del círculo: "))
    altura_cilindro = float(input("Ingrese la altura del cilindro: "))

    area_base_circulo = area_circulo(radio_circulo)
    volumen_del_cilindro = volumen_cilindro(altura_cilindro, area_base_circulo)

    print(f"Area del círculo: {area_base_circulo}")
    print(f"Volumen del cilindro: {volumen_del_cilindro}")

main()