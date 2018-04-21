# Euclid's algorithm
# GCD of a and b == GCD of smaller of them and bigger divided
# to smaller with the reminder
# Time complexity:
# Every iteration decreases one of the nums at least twice
# Num of steps <= log a + lob b
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a >= b:
            return gcd(a % b, b)
        else:
            return gcd(b % a, a)


print(gcd(3918848, 1653264))