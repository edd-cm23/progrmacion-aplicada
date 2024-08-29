# calcular 3er angulo de un triangulo 

import os 

os.system("cls")

angulo1 = int(input("dame el primer angulo:"))
angulo2 = int(input("dame el segundo angulo:"))

print(f'el tercer angulo es: {180 - (angulo1 + angulo2)} °')