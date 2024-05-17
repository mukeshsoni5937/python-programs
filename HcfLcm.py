def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a = int(input('Enter a number='))
b = int(input('Enter a number='))
lcm = (a*b)/gcd(a,b)
hcf = gcd(a,b)
print("HCF of ",a," and ",b," is==",hcf)
print("LCM of ",a," and ",b," is==",lcm)