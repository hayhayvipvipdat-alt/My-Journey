for x in range(3, 61, 3):
    if x == 39:
        print(x)
        break
    elif x % 10 == 0:
        print("TENT")
        continue
    elif x % 7 == 0:
        print("SEVEN")
    else:
        x *= x
        print(x)
         