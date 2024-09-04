# ingresa un numero entre 1 y 10 para convertir a romano

import os; os.system("cls") 
nrom = ('I','II','III','IV','V','VI','VII','VIII','IX','X')
print('Ingresa un numero entre 1 y 10 para convertir a romano')
n = int(input()) - 1


if n >= 0  and n < 10 :
    print(f'"{n+1}" es igual a "{nrom[n]}" en numeros romanos')

else :
    print(f'error {n + 1} ') 