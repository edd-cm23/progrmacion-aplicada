# calcular tiempo

import os ; os.system("cls")

horas = int(input('De cuantas horas desea conocer la equivalencia en dias, segundos y horas: '))

print(f'la equivalencia de {horas} horas es de:\n {horas/24:.3f} dia\n {horas *60} minutos\n {horas * 3600} segundos ')