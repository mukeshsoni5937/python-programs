try:
    num = float(input("Enter Numerator and Denominator=="))
    deno = float(input())
    result = num / deno

except ZeroDivisionError:
    print("Error: Division by zero!")

else:
    print("Division successful. Result=", result)

finally:
    print("End of program.")
