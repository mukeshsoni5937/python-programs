a = int(input("Enter Three Numbers== "))
b = int(input())
c = int(input())

if a >= b:
    if a >= c:
        print(a, "is the Largest")
    else:
        print(c, "is the Largest")
else:
    if b >= c:
        print(b, "is the Largest")
    else:
        print(c, "is the Largest")
