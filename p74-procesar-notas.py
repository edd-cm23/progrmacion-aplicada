import os ; os.system('cls')
calificaciones = []

while True :
    c = int(input('calificacion: '))
    if c != 111 :
        if c >= 0 and c <= 100:
            calificaciones.append(c)
        else :
            print('x')    
    else :
        break
   
suma = sum(calificaciones)
prom = suma / len(calificaciones)  
mp = []
for l in calificaciones:
    if l < prom :
       mp.append(l)
print('cantidad de calificacione: ',len(calificaciones))  
print('calificaciones :', calificaciones)    
print('suma de calificaciones :', suma)
print('promedio :', prom)      
print('mayores al promedio :',len(mp), mp) 
print('Mayor :' , max(calificaciones))
print('Menor :', min(calificaciones))