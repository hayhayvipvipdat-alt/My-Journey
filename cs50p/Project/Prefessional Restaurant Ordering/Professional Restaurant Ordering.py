# Professional Restaurant Ordering System - Single Item MVP

print("1. Espresso - 40k")
print("2. Cappuccino - 55k")
print("3. Cake - 60k")
print("4. Scone - 30k")
print("5. Sandwich - 75k")

try:
    item = int(input("What is your order? Pick the item number (1-5): ").strip())
except ValueError:
    print("Invalid input. Please enter a number from 1 to 5.")
    exit()
 
if item == 1:
    name = "Espresso"
    price = 40
elif item == 2:
    name = "Cappuccino"
    price = 55
elif item == 3:
    name = "Cake"
    price = 60
elif item == 4: 
    name = "Scone"
    price = 30
elif item == 5:
    name = "Sandwich"
    price = 75
else:
    print("Invalid item")
    exit()

try:
    quantity = int(input("Enter item quantity: ").strip())
except ValueError:
    print("Invalid input. Please enter 1 or more.")
    exit()

if quantity < 1:
    print("Quantity must be 1 or more.")
    exit()

subtotal = price * quantity

discount = subtotal * 0.05 if subtotal > 200 else 0

tax = (subtotal - discount) * 0.08

total = subtotal - discount + tax

print("----- RECEIPT -----")
print("Item:", name)
print(f"Price: {price:}k")
print("Quantity:", quantity)
print("-------------------")
print(f"Subtotal: {subtotal:.2f}k")
print(f"Discount: {discount:.2f}k")
print(f"Tax: {tax:.2f}k")
print(f"TOTAL: {total:.2f}k")
print("-------------------")
