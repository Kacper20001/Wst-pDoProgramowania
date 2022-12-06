""". Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
• Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
• Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
punktów nie występuje na liście, wyświetl odpowiedni komunikat
• Oblicz średnią punktów liczbę punktów z egzaminu
• Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
• Wyświetl punkty poniżej średniej
• Wyświetl punkty powyżej średniej"""

import random


"""Punkty=[]

for x in range(15):
    Punkty.append(round(random.uniform(0,50),2))"""

Punkty=[round(random.uniform(0,50),2) for x in range(15)]

print(Punkty)

Min=min(Punkty)
Max=max(Punkty)
print(f"Min:{Min}")
print(f"Max:{Max}")

sprawdzana_wartosc=int(input("podaj wartość do sprawdzenia"))
if sprawdzana_wartosc in Punkty:
    print(f"Wartość {sprawdzana_wartosc} ma index {Punkty.index(sprawdzana_wartosc)}")
else:
    print(f"wartość {sprawdzana_wartosc} nie występuje w liście ")

suma=sum(punkty)
ilosc= len(punkty)
srednia=suma/ilosc
print(f"Średnia wartość {round(srednia, 2)}")

mn=[]
wk=[]
for x in Punkty:
    if x<srednia:
        mn.append(x)
    else:
        wk.appernd(x)

print(mn, len(mn))
print(wk, len(wk))




