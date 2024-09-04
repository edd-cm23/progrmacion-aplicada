# calcular el promedio de 5 calificaciones

import os; os.system("cls") 

c1,c2,c3,c4,c5 = input('ingresa las 5 calificaciones separadas por coma "#,#,#,#,#"\n').split(",")
c1,c2,c3,c4,c5 =int(c1),int(c2),int(c3),int(c4),int(c5) 
prom = (c1 + c2 + c3 + c4 + c5) / 5 

if prom > 0  and prom < 6 :
    print(f'Calificacion :{prom}, reprobado')
 
elif prom < 7  :
    print(f'Calificacion :{prom}, Pasas de panzazo')

elif prom < 8  :
    print(f'Calificacion :{prom}, Muy bien, pues mejorar')  

elif prom < 9  :
    print(f'Calificacion :{prom}, Excelente sigue así')

elif prom >= 9 and prom <= 10  :
    print(f'Calificacion :{prom}, Perfecto tu esfuerzo valió la pena')    