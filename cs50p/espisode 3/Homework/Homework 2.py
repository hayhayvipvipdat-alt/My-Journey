for x in range(1, 101):
    if x % 11 == 0:
        print("STOP")
        break
    if "3" in str(x):
        continue
    if x % 7 == 0:
        print("SEVEN")
    else:
        print(x ** 3)