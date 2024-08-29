# calcular la hipotenusa de un triangulo rectangulo

import os 

os.system("cls")

ca = int(input("dame el cateto adyasente:"))
co = int(input("dame el cateto opuesto:"))

print(f'la hipotenusa del triangulo es: {float((pow(ca,2) + pow(co,2)))**0.5:.3f} ')
