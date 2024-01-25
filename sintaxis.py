#practica 2: sintaxis python

#soy un comentario

'''
soy un 
comentario
de 
varias lineas
'''

# 2. cadenas 
"""print ('soy una cadena')
print ("soy otra cadena")"""

"""
a='mi banda favorita es'
b="grupo marrano"
print(a+b) #se pueden concatenar valores de varias formas esta seria una de ellas 
print(a,b) #tambien se puede con una coma para indicar que esta va seguida de otra 
            #y esta agrega el espacio entre ellas

#cuenta los caracteres que hay incluyendo los espacios             
print(len(a))

print(b[2:5]) #toma caracter del 2 hasta el 5
print(b[:5]) #toma desce el inicio hasta el 5
print(b[2:]) #toma desde el segundo caracter hasta infinito
"""

#3 Variables
"""
#las variables no deben iniciar con numeros
x=5
y="jhon"
x=4.5  #en este caso al llamar la variable x va a tomar el ultimo valor que tiene asignado 

#el type nos ayuda a ver el tipo de variable que estamos utilizando
print(type(x))
print(type(y))


a=int(3) #indica que siempre sera un valor entero
b= str("3") #indica que siempre sera un valor tipo string
c=float(4.5)  #indica que siempre sera un valor flotante 

#el type nos ayuda a ver el tipo de variable que estamos utilizando
print(type(a))
print(type(b))
print(type(c))

import random
numero=random.randrange(1,20)
print(numero)


#4. Solicitud de datos

var1=input("introduce cualquier dato: ")
var2=str(input("introduce cadenas: "))
var3=int(input("introduce solo enteros: "))
var4=float(input("introduce numeros decimales: "))

print (var1,var2,var3,var4) #concatena los valores ingresados en cada input  


#5. Booleans, operadores de comparaacion y logica

print(10>9)
print(10== 9)
print(10< 9)
print(10>= 9)
print(10 !=9)
print(10<= 9)
#e estos casos devuelve valores true o false
"""

#logicos
x=1
print(x<5 and x<10)
print(x<5 or x<10)
print(not(x<5 and x<10))