# Imprime multiplos m entre 1 y n
import os; os.system("clear")
m = int(input("Multiplos de m ? "))
n = int(input("De 1 hasta n ? "))
cm = s = 0
for i in range(m, n+1):
    if i % m == 0:
        print(i, end=" ")
        s += i
        cm += 1

print(f"Los multiplos de {m} entre 1 y {n} fueron : {cm}, la suma de estos fue : {s}")