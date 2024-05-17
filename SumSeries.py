n = int(input("Enter the value of n== "))
sum_series = 0
for i in range(1, n + 1):
    sum_series += 1 / i
res = round(sum_series, 5)
print("Sum of the series 1 + 1/2 + 1/3 + ... + 1/n is==", res)