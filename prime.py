import math
def is_prime(num):
    #find square root
    if num <2:
        return False
    s = int(math.sqrt(num))
    for i in range(2,s+1):
        if num % i == 0:
            return False
    return True
print(is_prime(5))

def check_prime():
    for i in range(101):
        if is_prime(i):
            print(i)
check_prime()

