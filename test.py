def is_prime(x):
    if x >= 2:
        for i in range(2,x):
            if x % i == 0:
                return False
    else:
        return False
    return True

for i in range(0,200):
    if is_prime(i):
        print(i)