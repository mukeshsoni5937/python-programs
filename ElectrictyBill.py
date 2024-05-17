unit = int(input("Enter the unit consumed=="))
if 1 <= unit <= 200:
    total_charges = unit * 2.50
elif 201 <= unit <= 500:
    total_charges = unit * 3.50
elif unit > 500:
    total_charges = unit * 5.0
else:
    print("The Unit is invalid")
print("Total Charges==", total_charges,"Rupees")
