f = open("example2.txt", "w")
f.write("Hello, world!\n")
f.write("This is a sample text f.\n")
f.write("It contains multiple lines.\n")

f.close()

f = open("example2.txt", "r")
content = f.read()
print("File Content:\n", content)

f.close()

f = open("example2.txt", "r")
line = f.readline()
print("First Line:", line)
remaining_lines = f.readlines()
print("Remaining Lines:")
for line in remaining_lines:
    print(line.strip())  

f.close()

f = open("example2.txt", "a")
f.write("This is additional content appended to the f.\n")

f.close()

f = open("example2.txt", "r")
updated_content = f.read()
print("Updated f Content:\n", updated_content)

f.close()
