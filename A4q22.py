def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operand type!")
    except Exception as e:
        print("An unexpected error occurred:", e)
    else:
        print("Division successful. Result:", result)

print("Test 1=")
divide_numbers(10, 2)

print("\nTest 2=")
divide_numbers(10, 0)

print("\nTest 3=")
divide_numbers('a', 2)
