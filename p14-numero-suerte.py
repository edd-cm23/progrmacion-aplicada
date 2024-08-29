# conocer tu numero suerte

import os ; os.system("cls")

dia , mes , año =input('ingresa tu fecha de nacimiento en formato numerico separada por espacios: ').split() 
dia,mes,año = [int(dia), int(mes),int(año)]
print(f'{dia}/{mes}/{año} \n ')
print(f'Tu numero de la suerte es: {dia + mes + año}')