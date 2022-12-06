import random as rand
punkty = [round(rand.uniform(0, 50), 2) for x in range(15)]
print(punkty)
Min =min(punkty)
Max =max(punkty)
print(f'Min: {Min}')
print(f'Max: {Max}')
sp = float(input("Podaj wartość do sprawdzania: "))
if sp in punkty:
    print(f'Wartość {sp} ma index {punkty.index(sp)}')
else:
    print(f'Wartość {sp} nie wystempuje w liscie')
suma = sum(punkty)
ilosc = len(punkty)
s_war = suma / ilosc
print(f'Sriednia wartość punkyów {round(s_war, 2)}')
"""mn = []
we = []
for x in punkty:
    if x<s_war:
        mn.append(x)
    else:
        we.append(x)"""
mn= [x for x in punkty if x<s_war]
we= [x for x in punkty if x>s_war]
print(mn, len(mn))
print(we, len(we))