a=int(input("Enter Four Number == "))
b=int(input())
c=int(input())
d=int(input())
if(a>=b):
    if(a>=c):
        if(a>=d):
            print(a," Is the Largest")
        else:
            print(d," Is the Largest")
    else:
        if(c>=d):
            print(c," Is the Largest")
        else:
            print(d," Is the Largest")
else:
    if(b>=c):
        if(b>=d):
            print(b," Is the Largest")
        else:
            print(d," Is the Largest")
    else:
        if(c>=d):
            print(c," Is the Largest")
        else:
            print(d," Is the Largest")