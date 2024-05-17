base = int(input('Enter base value== '))
exponent = int(input('Enter exponent value=='))
ans = 1
for i in range(exponent):
    ans *=  base
print(f'{base}  raised to the power of {exponent} is== {ans}') 