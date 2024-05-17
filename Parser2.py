import parser  
print ("The input expression for the parser module")  
expression = "7 + 4"  
print (" Here we are parsing the input expression")  
parsing = parser.expr(expression)  
print(parsing)  
print (" Convert the parsed object into a code object")  
code = parsing.compile()  
print(code)  
print (" The parsed result is: ")  
res = eval(code)  
print(res)