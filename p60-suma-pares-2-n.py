#Se desea imprimir los pares de 2 a n y su suma
import os
os.system("cls") 

n = int(input("Dame un número: "))

suma = 0

for i in range(2, n+1, 2):
    for j in range(i, i+1):
        print(j, end=" ")
        suma += j 

print(f", La suma es = {suma}")