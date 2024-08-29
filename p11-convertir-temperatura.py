# convertir grados celcius a grados farenheit

import os ; os.system("cls")

celcius = float(input('ingresa los grados celcius (C°) que quieres convertir a farenheit(F°): '))

print(f'farenheit = {celcius * (9/5) + 32:.2f} °F')