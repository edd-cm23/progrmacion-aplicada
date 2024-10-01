# nombres y edades
import os;os.system('cls')
print('Nombres y edades\n')
print("Introduce los nombres y edades: * en nombre termina\n")
nombres=[]
edades=[]
while True:
    nombre=input("Nombre: ")
    if nombre!="*":
        nombres.append(nombre)
        edad=int(input("Edad: "))
        edades.append(edad) 
    else:
       break
print("Alumnos mayores de edad:")
for i in range(len(nombres)):
    if edades[i]>=18:
        print(f"Nombre: {nombres[i]} , Edad: {edades[i]}")

pos=edades.index(max(edades))
print(f"Alumno de mayor edad: {nombres[pos]}, {edades[pos]}")