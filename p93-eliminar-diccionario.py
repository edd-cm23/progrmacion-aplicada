
import os; os.system("cls")
municipios = {
    "Apozol": 1863,
    "Calera": 1868,
    "Fresnillo": 1554,
    "Guadalupe": 1821,
    "Jalpa": 1824,
    "Jerez": 1824,
    "Loreto": 1931,
    "Mazapil": 1824,
    "Momax": 1857
}

print("Diccionario de municipios:")
print(municipios)

del municipios["Apozol"]
print("\nsin Apozol:")
print(municipios)

fresnillo_value = municipios.pop("Fresnillo")
print("\nsin  Fresnillo:")
print(municipios)

momax_value = municipios.popitem()
print("\nsin Momax:")
print(municipios)

municipios.clear()
print("\nDiccionario vacio")
print(municipios)

