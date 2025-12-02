pre_input = None

for x in range(1,301):
    if pre_input == "BIG-THREE" and x % 5 == 0:
        print("CHAIN")
        break
    elif "8" in str(x):
        pre_input = None
        continue
    elif x > 120 and x % 3 == 0:
        print("BIG-THREE")
        pre_input = "BIG-THREE"
        continue
    elif x % 4 == 0 and x % 7 == 0:
        print("FOURSEVEN")
        pre_input = "FOURSEVEN"
        continue
    elif x % 11 == 0:
        print("ELEVEN")
        pre_input = "ELEVEN"
        continue
    else:
        print(x)
        pre_input = None