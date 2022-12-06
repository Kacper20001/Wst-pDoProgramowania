"""• Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy podaje
użytkownik. Wyświetl listę.
• Utwórz drugą listę zestaw_2 zawierającą liczby losowe z przedziału [5, 15]. Liczbę elementów listy
podaje użytkownik. Wyświetl listę.
• Pobierz od użytkownika liczbę. Napisz instrukcję warunkową, która na podstawie wartości
zapisanych w listach wyświetli jeden z poniższych komunikatów: „Liczba z zestawu 1”, „Liczba z
zestawu 2” albo „Nie ma takiej liczby w obu zestawach”.
• Utwórz listę zestaw_1_2 będącą złączeniem wartości z list zestaw_1 oraz zestaw_2. Posortuj i wyświetl
listę."""
import random
zestaw_1=[]
x=int(input("podaj liczbę elementów"))

for i in range(x):
    z=random.randint(1,10)
    zestaw_1.append(z)
print(zestaw_1)

y=int(input("podaj długość liczby elementow 2 liczby"))
zestaw_2=[random.randint(5,15) for a in range(y)]
print(zestaw_2)

liczba=int(input("sprawdz sowja liczbe"))
if liczba in zestaw_1 and liczba in zestaw_2:
    print("liczba jest w obu zestawach ")
elif liczba in zestaw_2:
    print("liczba z zestawu 1")
elif liczba in zestaw_1:
    print("liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w obu zestawach")

""" Utwórz listę zestaw_1_2 będącą złączeniem wartości z list zestaw_1 oraz zestaw_2. Posortuj i wyświetl
listę"""

zestaw_1_2= zestaw_1+zestaw_2
zestaw_1_2.sort()
print(zestaw_1_2)
#tylko trzeba zakomentować funkcje