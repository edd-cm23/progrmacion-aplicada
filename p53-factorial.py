# Imprime el factorial de un número
print('Imprime el factorial de un número \n')
n = int(input('De que numero deseas factorial? '))
f = 1
for i in range(1,n+1):
    f = f * i
    print(f"{i} {'x' if i!=n else''}",end=" ")
print(f'\nEl factorial es: {f}')