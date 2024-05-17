dia=int(input("Enter the diameter of the steel bar in milli meter== ")) 
length=int(input("Enter the length of the steel bar in meter== " ))
weight=((dia**2)/162)* length
print("Weight of steel bar in kg per meter==", round(weight,2))