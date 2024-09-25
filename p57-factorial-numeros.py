# Imprime el factorial de n números

print('Calcula el factorial de n números:\n')
n = int(input('Cuantos números ? '))
for i in range(1,n+1):
    f=1
    print(f'{i}! = ', end='')
    for i in range(1,i+1):
        f *= i
    print(f)