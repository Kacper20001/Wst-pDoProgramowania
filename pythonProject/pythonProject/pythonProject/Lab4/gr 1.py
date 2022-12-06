"""Grupa 1. Użytkownik podaje dwie liczby zmiennoprzecinkowe. Sprawdź czy suma tych liczb mieści się w przedziale [0, 20]."""
a=float(input("podaj liczbę rzeczywistą"))
b=float(input("podaj 2 liczbe rzeczywista"))
if a+b>=0 and a+b <=20:
    print (" suma liczb mieści się w przedziale od 0 do 20 ")
else:
    print(" suma liczb nie mieści się w przedziale od 0 do 20")