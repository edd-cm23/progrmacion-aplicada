# numeros del 1 al 100

import os; os.system("cls") 

n = int(input('hasta que numero quieres llegar? '))
p = int(input('de cuanto en cuanto quieres contar? '))

c = 0
while c <= n :
    print(c, end=" ")
    c+=p