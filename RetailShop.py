item_name = input("Enter the item name== ")
price_per_unit = float(input("Enter the price per unit=="))
quantity = int(input("Enter the quantity== "))
total_cost = quantity * price_per_unit
print("Total cost:", total_cost)
payment = float(input("Enter the payment amount== "))
pay_change = payment - total_cost
print("Item=", item_name)
print("Payment=", payment)
print("Change=", pay_change)
