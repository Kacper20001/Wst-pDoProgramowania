a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a<b:
    while a <= b:
        if a%2 == 1:
            a = a + 1
            continue
        print(a, end = ' ')
        a = a + 1
else:
    while b <= a:
        print(b)
        b = b + 1
