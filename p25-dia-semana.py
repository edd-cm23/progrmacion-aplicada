# ingresa un numero entre 1 y 7 para saber el dia de la semana

import os; os.system("cls") 
semana = ('lunes','martes','miercoles','jueves','viernes','sabado','domingo')
print('Ingresa un numero de dia entre 1 y 7')
ndia = int(input()) - 1


if ndia >= 0  and ndia < 7 :
    print('Hoy es: ',semana[ndia])

else :
    print(f'No existe el dia: {ndia + 1} ') 