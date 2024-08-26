# Calcular el promedio de 3 calificaciones
print('Calculando el promedio de 3 calificaciones')
print('Dame 3 calificaciones separadas por espacios:')
c1,c2,c3 = input().split()# .split(separador, las separaciones maximas que hace) es un metodo que separa los valores 
c1,c2,c3 = [int(c1), int(c2),int(c3)] #convierte el sting en tipo entero
prom = (c1+c2+c3)/3
print(f'El promedio de : {c1},{c2},{c3} es {prom}')