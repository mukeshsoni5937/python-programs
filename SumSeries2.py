n = int(input("Enter the value of n=="))
sum = 0
for i in range(1, n + 1):
    sum = sum + (1 / (i ** i))
res = round(sum, 5)
print("Sum of the series 1 + 1/2^2 + 1/3^3 + ... + 1/n^n is==",res)