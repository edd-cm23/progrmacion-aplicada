# Se desea procesar los empleados de una empresa de muebles

import os; os.system("cls")


empleados = []
h = 0
m = 0

print("Inicial ", empleados, len(empleados))

while True:
    datos = {}
    print("al pedir el nombre escribe un '*' para finalizar ")
    nombre = input("Nombre : ")
    if nombre != "*" :
        datos["nombre"] = nombre
        datos["edad"] = int(input("Edad: "))
        datos["sexo"] = input("Sexo(h/m): ")
        datos["pasatiempo"] = input("Pasatiempo: ")
        datos["salario"] = float(input("Salario: "))
        empleados.append(datos)
    else:
        break

print("Todos ", empleados)

print("\nDatos de tabla")
for k in empleados[0].keys():
    print(f"{k}", end=" ")
print()    
for emp in empleados:
    for x in emp.values(): 
        print(f"{x}", end=" ")
    print()        

print(f"\nResumen:")
print(f"\nEmpleados: {len(empleados)}")

for n in empleados:
    if empleados[empleados.index(n)].get('sexo') == 'm':
        m = m + 1
    elif empleados[empleados.index(n)].get('sexo') == 'h':    
        h = h + 1
print (f'Mujeres: {m}\nHombres: {h}')

pt = {}

for p in empleados : 
    pasa_tiempo = empleados[empleados.index(p)].get('pasatiempo')
    if pasa_tiempo not in pt :
        pt[pasa_tiempo] = 1
    else :
        pt[pasa_tiempo]+= + 1

print('Pasatiempos: ')        
for p,c in pt.items():
    print(f' {p}/{c}', end = ',')        
print()

suma_edad = 0
for e in empleados : 
    suma_edad = suma_edad + empleados[empleados.index(e)].get('edad')
    prom_edad = suma_edad / len(empleados)
print(f"Edad--> Suma: {suma_edad}, promedio: {prom_edad}")

suma_salario = 0
for sal in empleados : 
    suma_salario +=  + empleados[empleados.index(sal)].get('salario')
    prom_salario = suma_salario / len(empleados)
print(f"Edad--> Suma: {suma_salario}, promedio: {prom_salario}")

mayor,menor = 0,0
nombre_mayor , nombre_menor = '' , ''
for e in empleados :
    if  empleados[empleados.index(e)].get('edad') > mayor :
        mayor = empleados[empleados.index(e)].get('edad')
        nombre_mayor = empleados[empleados.index(e)].get('nombre')

    elif  menor < empleados[empleados.index(e)].get('edad') :
        menor = empleados[empleados.index(e)].get('edad')
        nombre_menor = empleados[empleados.index(e)].get('nombre')
    else :
        menor = empleados[empleados.index(e)].get('edad')
        nombre_menor = empleados[empleados.index(e)].get('nombre')
print (f'\n{nombre_mayor} de {mayor} es el mayor,{nombre_menor} de {menor} es el menor')    