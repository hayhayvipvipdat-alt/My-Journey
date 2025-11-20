print("1 - Coffe")
print("2 - Tea")
print("3 - Juice")

x = int(input("What's is your order ? Enter the item number: "))

match x:
    case 1:
        print("You chose Coffe")
    case 2:
        print("You chose Tea")
    case 3:
        print("You chose Juice")
    case _:
        print("Invalid option") 

