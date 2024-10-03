import os; os.system('cls')
ciudades = []
consonantes = ''
n=0
while True:
    ciudad = input('Introduce una ciudad ( $ para detenerse): ')
    if ciudad == '$':
        break
    ciudades.append(ciudad)

print(f'Ciudades: {len(ciudades)}, {ciudades}')

ciudades.sort(reverse=True)
print("\nLista de ciudades ordenada en orden descendente:", ciudades)

for x in range(len(ciudades)) :
    consonantes = str(ciudades[x]).startswith(('a','e','i','o','u'))
    if consonantes == False :
   # n = ciudades.index(ciudades[x])
         n += 1
         print ('Ciudades consonante: ',n,ciudades[x])
       