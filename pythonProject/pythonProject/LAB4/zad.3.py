"""Utwórz pustą listę zwierzeta. Następnie
• Dodaj kilka nazw zwierząt do listy
• Posortuj listę
• Wyświetl pierwszy oraz trzy ostatnie elementy na liście
• Wyświetl informację o liczbie zwierząt na liście"""


zwierzeta=[]
for x in range(6):
    x= str(input('podaj nazwy zwierząt'))
    zwierzeta.append(x)
    zwierzeta.sort
print(zwierzeta[0],zwierzeta[-3:])
print(len(zwierzeta))
