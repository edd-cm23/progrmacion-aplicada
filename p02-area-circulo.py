# Calcular el area de un circulo

import math  #importar libreria math
print('Calculando el area de un circulo:\n')
print('Dame el radio: ')

radio = float(input())
area = math.pi * radio ** 2 #usa el objeto pi que es una constante de la libreria math
print(f'El circulo de radio {radio} tiene un area de {area}')