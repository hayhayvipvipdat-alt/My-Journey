for x in range(1, 101):
    if x % 13 == 0:
        print("STOP")
        break
    elif "5" in str(x):
        continue
    elif x % 4 == 0 and x % 6 == 0:
        print("FOUR-SIX")
    elif x % 4 == 0:
        print("FOUR")
    elif x % 6 == 0:
        print("SIX")
    else:
        print(x)