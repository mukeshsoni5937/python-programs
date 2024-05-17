import math
x_degrees = float(input("Enter the value of x in degrees=="))
num_terms = int(input("Enter the number of terms=="))
def sine(x_degrees, num_terms):
    x_radians = math.radians(x_degrees)
    sum = 0
    for n in range(num_terms):
        term = ((-1) ** n) * (x_radians ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sum += term
    print("Sum of the sine expansion==", sum)
sine(x_degrees, num_terms)