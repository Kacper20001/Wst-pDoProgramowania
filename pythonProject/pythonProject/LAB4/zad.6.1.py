""". Zmodyfikuj skrypt z poprzedniego zadania tak, aby utworzyć listę Y, wykonując operację: Y = X[:]"""
x=list(range(1,11))
print(x)
print(x[-3:])
x[:0]=x[-3:]
x[-3:]=[] # to samo co del
print(x)

y=[]
y=x[:] # shallow copy
print(y)
y[1]=5
print(x)
print(y)