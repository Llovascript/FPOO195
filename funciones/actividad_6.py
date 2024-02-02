"""
#1.-total de una factura tras aplicar IVA
def calcular_total_con_iva():
    cantidad = float(input("Ingrese el monto sin IVA: "))
    iva = input("Porcentaje de IVA: ")
    
    if iva:
        iva = float(iva)
    else:
        iva = 21

    iva2 = cantidad * (iva / 100)
    total = cantidad + iva2
    return total

total_con_iva = calcular_total_con_iva()
print(f"Total con IVA: {total_con_iva}")
"""

"""
#2.- area de un circulo y volumen del cilindro
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
"""

#3.-número decimal a binario y binario a decimal
def bindec(num):
    S = 0
    i = 0
    n = num
    
    while n >= 1:
        d = n % 10
        S = S + d * 2 ** i
        n = n // 10
        i = i + 1
    print("Es en decimal:", S)

def decbin(num):
    n = num  
    resultado_binario = ""
    
    while n > 0:
        residuo = n % 2
        resultado_binario = str(residuo) + resultado_binario
        n = n // 2
    print("Es en binario:", resultado_binario)


num_binario = int(input("Ingrese un número binario: "))
bindec(num_binario)
num_decimal = int(input("Ingrese un número decimal: "))
decbin(num_decimal)
