Name = input("What's your name ? ")

match Name: 
    case "Harry" | "Hermione" | "Ron":
        print("Gryfindor")
    case _:
        print("Fuck off")