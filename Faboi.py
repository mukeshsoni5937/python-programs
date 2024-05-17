def fibonacciSeries(n):                   
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacciSeries(n - 1) + fibonacciSeries(n - 2)

n = int(input("Enter nth Term=="))
print("Fibonacci series==")
for n in range(0, n):
	print(fibonacciSeries(n))