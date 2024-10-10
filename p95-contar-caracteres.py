
import os; os.system("cls")
cadena = input("Ingresa una cadena: ")

contador = {}

for x in cadena:
    if x in contador:
       
        contador[x] += 1
    else:
        contador[x] = 1

print("Cantidad de apariciones de cada carácter:")
print(contador)