# file_content = """
# This is a sample text file.
# It contains multiple lines of text.
# Each line demonstrates a different feature of the file.
# You can use this file to test the program.
# """

# file_name = "example.txt"
# with open(file_name, 'w') as file:
#     file.write(file_content)

# print(f"File '{file_name}' created successfully.")

def display_file_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")

# Example usage:
file_name = input("Enter the name of the file= ")
display_file_contents(file_name)