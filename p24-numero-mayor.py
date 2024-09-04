# revisar cual de los 3 numeros ingresados es mayor

import os; os.system("cls") 

print('Ingresa 3 numeros separados por coma ","')
n1, n2, n3 = input().split(",")
n1, n2, n3 = [int(n1), int(n2), int(n3)]

if n1 > n2  and n2 > n3 :
    print(f'de los numeros({n1},{n2},{n3}), {n1} es el mayor')

elif n3 > n1  and n2 > n3 :
    print(f'de los numeros({n1},{n2},{n3}), {n2} es el mayor') 

else :
    print(f'de los numeros({n1},{n2},{n3}), {n3} es el mayor') 