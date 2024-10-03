import random, os
os.system('cls')
l1 = []
l2 = []
l3 = []

for x in range(5):
    l1.append(random.randint(1,100))
    l2.append(random.randint(1,100))
for x in range(5):
    l3.append(l1[x] * l2[x])
print("\nListas :")
print(f"Lista 1 : {l1}")
print(f"Lista 2 : {l2}")
print(f"Lista 3 : {l3}")