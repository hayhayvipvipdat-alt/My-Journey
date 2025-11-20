# Professtional Restaurant Ordering System - Sing Item MVP

print("1. Espresso - 40k")
print("2. Cappuchino - 55k")
print("3. Cake - 60k")
print("4. Scone - 30k")
print("5. Sandwich - 75k")

x = int(input("What's is your order ? Pick the item number: "))
 
if x == 1:
    name = "Espresso"
    price = 40
    print(" Espresso - 40k")
elif x == 2:
    name = "Cappuchino"
    price = 55
    print("Cappuchino - 55k")
elif x == 3:
    name = "Cake"
    price = 60
    print("Cake - 60k")
elif x == 4: 
    name = "Scone"
    price = 30
    print("Scone - 30k")
elif x == 5:
    name = "Sandwich"
    price = 75
    print("Sandwich - 75k")
else:
    print("Invalid item")

y = int(input("Enter item quantity: "))

if x < 1: 
    print("Error")


Subtotal = price * y

if Subtotal > 200:
    Discount = Subtotal + 5 / 100 * Subtotal
else:
    Discount = 0 

Tax = Discount + 8 / 100 * Subtotal

Total = Subtotal - Discount + Tax

print("----- RECEIPT -----")
print("Item:", name)
print(f"Price:", "{price}k")
print("Quantity:", "{y}k")
print(f"Subtotal:", "{Subtotal}k")
print(f"Discount: -", "{Discount}k")
print(f"Tax:", "{Tax}k")
print(f"Total:", "{Total}k")
print("-------------------")
