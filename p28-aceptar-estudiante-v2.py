# aceptar estudiante a la universidad kitty kat SA

import os; os.system("cls") 

aspirante = []
print('ingrese NOMBRE, SEXO, EDAD, CALIFICACION_1,CAL_2,CAL_3 ')

for i in range(0,6) :
    aspirante.append(input()) 

prom = (float(aspirante[3]) + float(aspirante[4]) + float(aspirante[5])) / 3
print(aspirante ,'promedio:', prom ,'\n');  
if aspirante[1] == 'm' and int(aspirante[2]) > 21 and prom >= 8 :
    print('ACEPTADO')
else : 
    print('no cumple los requisitos')