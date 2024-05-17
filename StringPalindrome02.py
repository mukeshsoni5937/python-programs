def reverse_string(input_str):
    return input_str[::-1]
def is_palindrome(input_str):
    reversed_str = reverse_string(input_str)
    return input_str == reversed_str
inpstr = input("Enter a string==")   
revstr = reverse_string(inpstr)
print(f"Reversed string== {revstr}")
if is_palindrome(inpstr):
    print("The Given String ",inpstr," is a Palindrome") 
else: 
    print("The Given String ",inpstr," is Not a Palindrome")
