# Pedir al usuario que ingrese los colores disponibles
import os; os.system("cls")
colores = input("Ingrese los colores disponibles (separados por comas): ").split(",")
print("\nLos colores", colores)
for color1 in colores:
    for color2 in colores:
        if color1 != color2:

            print(f"{color1.strip()} y {color2.strip()}")