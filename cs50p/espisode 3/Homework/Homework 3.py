y = ""
first = False
for x in range(1, 101):
    if x % 7 == 0 and first == False:
        print("First_Seven")
        first = True
        y = "First_Seven"
        continue
    if x % 10 == 0 and y == "BIG":
        print("STOP-BIG")
        break
    if "7" in str(x):
        continue
    if x > 50 and x % 5 == 0:
        print("BIG")
        y = "BIG"
        continue
    if x % 4 == 0:
        print("FOUR")
        y = "FOUR"
        continue
    else:
        print(x)
        y = str(x)

        