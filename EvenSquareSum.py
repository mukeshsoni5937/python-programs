n = int(input("Enter the value of n=="))
sum_squares = 0
for i in range(2, n + 1, 2):
    sum_squares += i ** 2
print("Sum of squares of even numbers up to", n, "is==", sum_squares)