print("string length")
st = "Hello world !"

print(len(st))
print("string Index")
st = "Hello world ! Hello Hello"
print(st.index("Hello"))
st2 = "This is a sentence"
st1 = st2.index("is")
print(st1)
print("String strip")
st = "      Hello world !     "
print(st)
print(st.strip())

print("string lstrip")
st = '  hello world'
print(st)

print(st.lstrip())
print("string  Rstrip")
st = 'Hello world !'
print(st)
print(st.rstrip())
print("String split")
st = "India is a great country"
print(st.split())
print("String Join")
st3  = "Hello world!"
st4 = " "
print(st4.join(st3))
print("string find")
st = "hello world ! Hello world !"
print(st.find("hello", 10, 20))
print(st.find("Hello"))
print(st.find("hee"))
print("string upper")
st = "hello world "
print(st.upper())
print("string lower")
print(st.lower())
print("string starts with")
st = "hello world!"
if(st.startswith('he')):
    print("TRUE")
else:
    print("false")
if(st.startswith('hee')):
    print("TRUE")
else:
    print("false")
print()
print("string endswith")
st = 'hello world !'
if(st.endswith('world!')):
    print("TRUE")
else:
    print("False")
if(st.endswith('!')):
    print("True")
else:
    print("false")
print()
print("string count")
st = 'hello world ! hello hello'
print(st.count('hello', 12, 25))
print(st.count('hello'))
print("string concatanation")
st = 'Hello'
st2 = "world"
print(st+st2)