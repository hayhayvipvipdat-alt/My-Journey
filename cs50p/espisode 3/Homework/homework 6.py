def is_prime(x):
    if x < 2:
        return False
    i = 2 
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

nf_flag = False
after_nf_count = 0

for x in range(1, 301):
    if "2" in str(x):
        continue
    elif x % 9 == 0 and x % 5 == 0:
        print("NINE-FIVE")
        nf_flag = True
        continue
    elif x % 12 == 0:
        if nf_flag:
            print("AFTER-NF")
            after_nf_count += 1
            if after_nf_count == 3:
                break
            continue
        else:
            print("TWELVE")
            continue
    elif is_prime(x) == True:
        if x > 200:
            print("PRIME+")
            continue
        else:
            print("prime")
            continue
    else:
        print(x)

    