"""Załóżmy, że lista X składa się z 10 elementów. Przenieś ostatnie trzy elementy z końca na początek listy
bez zmiany ich oryginalnej kolejności.
• Utwórz listę Y, wykonując operację: Y = X. Następnie zmień jeden z elementów listy Y. Wyświetl obie listy
na ekranie"""

x=list(range(1,11))
print(x)
print(x[-3:])
x[:0]=x[-3:]
x[-3:]=[] # to samo co del
print(x)

y=[]
y=x
print(y)
y[1]=5
print(x)
print(y)