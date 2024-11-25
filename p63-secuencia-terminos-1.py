#Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:

import os
import math

os.system("cls") 

n = int(input("¿Cuántos términos?? "))

suma = 0

terminos = []

for i in range(1, n + 1):
    termino = 1 / math.factorial(i)
    terminos.append(f"1/{i}!")
    suma += termino

print("Salida:", " + ".join(terminos), ", suma:", suma)
