# resisar si los 3 numeros ingresados son consecutivos

import os; os.system("cls") 

print('Ingresa 3 numeros consecutivos separados por coma ","')
n1, n2, n3 = input().split(",")
n1, n2, n3 = [int(n1), int(n2), int(n3)]

if n2 == n1 + 1  and n3 == n2 + 1 :
    print(f'los numeros({n1},{n2},{n3})son consecutivos')

elif n2 == n3 + 1  and n1 == n2 + 1 :
    print(f'los numeros({n1},{n2},{n3})son consecutivos')    

else :
     print(f'los numeros({n1},{n2},{n3}) "NO" son consecutivos')