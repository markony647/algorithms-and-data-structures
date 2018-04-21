
def fib_exponential(n):
    assert n >= 0
    if n  <= 1:
        return n
    else:
        return fib_exponential(n - 1) + fib_exponential(n - 2)

cache = {}


def fib_with_cache(n):
    assert n >= 0
    if n not in cache:
        if n <= 1:
            cache[n] = n
        else:
            cache[n] = fib_with_cache(n - 1) + fib_with_cache(n - 2)
    return cache[n]

print(fib_with_cache(5))


# Liner time
def fib_super_performance(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1

print(fib_super_performance(800))


