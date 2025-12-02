def is_prime(x):
    if x < 2:
        return False
    i = 2 
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

first_twenty = False
chain_count = 0

for x in range(1, 301):
    if "7" in str(x):
        continue
    if x % 20 == 0:
        print("FIRST-TWENTY")
        first_twenty = True
        continue
    if first_twenty == True and x % 9 == 0:
        print("CHAIN-9")
        chain_count += 1
        if chain_count == 4:
            break
        continue
    if x % 3 == 0 and x % 8 == 0: 
        print("THREE-EIGHT")
        continue
    if is_prime(x):
        if x < 150:
            print("prime")
            continue
        else:
            print("PRIME+")
        continue
    else:
        print(x)
