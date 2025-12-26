while True:
    try:
        x = int(input("How long is your password?"))
    except ValueError:
        print("Invalid input")
        continue
    if x < 6:
        print("Invalid input")
        continue
    print("Valid Length")
    break
