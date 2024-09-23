# pares e impares de 1 a n y su suma
import os
while(True):
    os.system('clear')
    print('Pares e impares de 1 a n y su suma \n')
    n = int(input('Hasta donde deseas los numeros? '))
    s = 0
    print("\nNumeros pares:")
    for i in range(1,n+1,2):
        print(i,end=' ')
        s += i
    print(f'\nSuma pares: {s}')
    s = 0
    print("\nNumeros impares:")
    for i in range(2,n+1,2):
        print(i,end=' ')
        s += i
    print(f'\nSuma impares: {s}')
    res = input('\n\nDeseas continuar (S/N) ? ').upper()
    if res=='N':
        break
print('\n\nGracias por utilizar este programa')