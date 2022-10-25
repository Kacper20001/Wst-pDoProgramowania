print("""Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie""")
x= float(input("wybierz 1 liczbę"))
y= float(input("wybierz 2 liczbę"))
z= int(input("wybierz działanie"))

if z==1:
    a=x+y
elif z==2:
    a=x-y
elif z==3:
    a=x*y
elif z==4:
    if y==0:
        print("nie można wykonać takiego działania")
        exit()
    a=x/y
elif z==5:
    c=x**y
else:
    print("nie dokonałeś żadnego wyboru")
    exit()
print("twój wynik to ",a)
