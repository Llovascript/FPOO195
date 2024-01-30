"""
#break
cont = 1
while cont <= 5:
    print(cont)
    if cont == 3:
        break
    cont += 1
else: 
    print("el bucle ha terminado")    
"""
"""
# continue
cont = 0
while cont < 5:
    cont += 1
    if cont == 3:
        continue
    print(cont)
else: 
    print("el bucle ha terminado")
"""

#else 
cont = 1

while cont <= 10:
    print(cont)
    cont += 1
else:
    print("el bucle ha terminado")