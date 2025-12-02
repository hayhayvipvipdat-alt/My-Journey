while True:
    try:
        x = int(input("How long is your password?"))
    except ValueError:
        print("Invalid input")
    if x < 6:
        print("Invalid input")
        continue
    else:
        print("Valid Length")
        break
