l1=int(input("Podaj 1 liczbę: "))
l2=int(input("Podaj 2 liczbę: "))

if l2<l1:
    l1,l2=l2,l1
while l1<=l2:
    print(l1)
    l1+=1


