try:
    file = open("example1.txt", "w")
    file.write("Hello, world!")
    raise Exception("Intentional Exception")

except IOError as e:
    print("IOError occurred:", e)

except Exception as e:
    print("Exception occurred:", e)

finally:
    try:
        file.close()
    except UnboundLocalError:
        print("File was not opened.")
    else:
        print("File closed successfully.")

print("End of program.")
