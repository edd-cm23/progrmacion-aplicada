#Conversión de temperaturas de centigrados a Fahrenheit

print("Conversión de temperaturas de centigrados a Fahrenheit y viceversa \n")
print("[1] Convertir Celcius")
print("[2] Convertir Fahrenheit")
print("[3] Salir")

opcion = int(input("Elige la opción: \n"))

if opcion == 1:
    print("\nConvirtiendo Fahrenheit a Centigrados\n")
    temp = float(input("Ingresa los grados Fahrenheit: "))
    r = (temp - 32) * 5 / 9
    print(f'{temp}° Fahrenheit, equivalen a {r:.2f}° Centigrados')
elif opcion == 2:
    print("\nConviritiendo Centigrados a Fahrenheit\n")
    temp = float(input("Ingresa los grados Centigrados"))
    r = ( temp * 9 / 5 ) + 32
    print(f"{temp}° Fahrenheit, equivalen a {r:.2f}° Centigrados")
elif opcion == 3:
    print("\nSaliendo del programa... ")
else:
    print("Opción erronea")

print("\nProceso terminado.")