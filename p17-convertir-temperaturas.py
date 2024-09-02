#Conversión de temperaturas de centigrados a Fahrenheit

print("Conversión de temperaturas de centigrados a Fahrenheit \n")
opcion = str.upper( input('Convertir a [C]entigrados o convertir a [F]ahrenheit') )

if opcion == 'C':
    print("\nConvirtiendo a Centigrados\n")
    temp = float(input("Ingresa los grados Fahrenheit: "))
    r = (temp - 32) * 5 / 9
    print(f'{temp}° Fahrenheit, equivalen a {r:.2f}° Centigrados')
else :
    print("\nConviritiendo a Fahrenheit\n")
    temp = float(input("Ingresa los grados Centigrados"))
    r = ( temp * 9 / 5 ) + 32
    print(f"{temp}° Fahrenheit, equivalen a {r:.2f}° Centigrados")