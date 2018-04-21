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


def gcd2(a, b):
    while a and b:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


print(gcd(3918848, 1653264))
print(gcd(58, 46))


# Very inefficient algorithm
def naive_gcd(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == b % d == 0:
            return d
    return d

print(naive_gcd(46, 58))
print(naive_gcd(3918848, 1653264))