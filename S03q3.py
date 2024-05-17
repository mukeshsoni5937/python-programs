num = 0
for i in range(1,5):
    num = int((i*(i+1))/2)
    for j in range(i,5):
        print(" ", end=" ")
    for k in range(i):
        print(num, end=" ")
        num -= 1
    print()