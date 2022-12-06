"""Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
wykorzystaniem pętli while"""
i=1 #odkąd liczymy
a=int(input("wpowadź liczbę studentów"))
suma=0
while i<=a:
    y=int(input(f"podaj wynik {i} studenta"))
    i+=1
    suma+=y
print(suma/a)


