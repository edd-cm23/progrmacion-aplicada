#desea imprimir los números de 1 a n de 10 en 10
import os
os.system("cls")  

n = int(input("Dame un número: "))

for i in range(1, n+1, 10):
    for j in range(i, i+1):
        print(j, end=" ")

print()  