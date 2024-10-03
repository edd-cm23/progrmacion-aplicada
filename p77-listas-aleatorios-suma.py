# listas con aleatorios
import random, os
os.system('cls')
l1 = []
l2 = []
l3 = []

for x in range(10):
    l1.append(random.randint(1,10))
    l2.append(random.randint(1,10))
pos = list(enumerate(l1))   
for x in range(10):
    
    if l1[x] % 2 != 0 and l2[x] % 2 != 0:
        l3.append(l1[x] + l2[x]) 
        print(pos[x])
        
print("\nListas procesadas:")
print(f"Lista 1 : {l1}")
print(f"Lista 2 : {l2}")
print(f"Lista 3 : {l3}")
print(f"pos : {pos}")
print(list(pos))