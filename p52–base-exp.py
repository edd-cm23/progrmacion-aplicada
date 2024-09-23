# Dado un número entero base y un exponente exp, calcular la potencia de base elevado a exp
import os; os.system("clear")
base = int(input("Base ? "))
exp = int(input("Exponente ? "))
res = 1
for _ in range(exp):
    res *= base
print(f"{base} ^ {exp} = {res}" )