import math
pf=float(input("Enter the Power factor pf (lagging)=="))
I=float(input("Enter the Current I== "))
V=float(input("Enter the Voltage V== "))
P=math.sqrt(3)*pf*I*V
print("Electrical Current in Three Phase AC Circuit ==", round(P,3))