import os; os.system('cls')
n = int(input('Cuantos numeros impares quieres en la lista? '))

impares = []

for i in range(1, 2*n, 2):
    impares.append(i)

print(f' números impares: {impares}')

suma_impares = sum(impares)
promedio_impares = suma_impares / len(impares)
print(f'Suma de los números impares: {suma_impares}')
print(f'Promedio de los números impares: {promedio_impares}')

divisibles_por_3 = [num for num in impares if num % 3 == 0]
suma_divisibles = sum(divisibles_por_3)
print(f'Números divisibles entre 3: {divisibles_por_3}')
print(f'Suma de los números divisibles entre 3: {suma_divisibles}')

buscar_num = int(input('Introduce un número para buscar: '))

if buscar_num in impares:
    posicion = impares.index(buscar_num)+1
    print(f'El número {buscar_num} está en la lista en la posición {posicion}.')
else:
    print(f'x')