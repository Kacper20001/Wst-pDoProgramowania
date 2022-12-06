"""Zadanie 7 (7.py) Za pomocą pętli for wypisz na ekranie ciągi liczb:
• 1, 2, 3, ... , 99, 100
• 100, 99, ... , 2, 1, 0
• 7, 14, 21, ... , 70, 77
• 20, 18, ... , 2, 0"""

for x in range(1,101):
    print(x, end=" ")
print()
for i in range (100,-1,-1):
    print(i, end=" ")
print()
for z in range(7,84,7):
    print(z, end=" ")
print()
for y in range(20,-2,-2):
    print(y, end=" ")

