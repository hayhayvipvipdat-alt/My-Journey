x = input("What's your username? ")
y = int(input("What's your password? "))

match x:
    case "admin":
        if y == 1234:
            print("Accces Granted")
        else:
            print("Wrong password")
    case _:
        print("Wrong username")
