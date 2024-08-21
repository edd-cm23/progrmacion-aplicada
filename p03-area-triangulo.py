# Calcular el area de un triangulo
print('Calculando el area de un triangulo:\n')
print('Dame la base y la altura separados por un Enter')
base, altura = int(input()), int(input()) # introducir dos variables seguidas
area = base * altura / 2 # si son operaciones del mismo nivel comienza de izquierda a derecha en prioridad
print(f'El triangulo de base {base} y altura {altura} tiene un area de {area}')
