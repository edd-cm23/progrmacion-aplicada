# suma de n números introducidos por el usuario:
print('Suma de n números introducidos por el usuario:')
cuantos = int(input('Cuantos numeros ? '))
suma = 0

for i in range(1,cuantos+1):
    n = int(input(f"Número {i} ? "))
    suma += n

print(f'\nLa suma es {suma}')