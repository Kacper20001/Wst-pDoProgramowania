import random
#zestaw_1=[]
x=int(input("podaj liczbę elementów"))

#for i in range(x):
 #   z=random.randint(1,10)
  #  zestaw_1.append(z)
#print(zestaw_1)

lista=[random.randint(1,10) for i in range(x)]
print(lista)

