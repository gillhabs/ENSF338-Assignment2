# original func
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

# optimized func
def optimized_func(n, cache={0:0, 1:1}):
    if n in cache:
        return cache[n]
    else:
        cache[n] = optimized_func(n-1) + optimized_func(n-2)
        return cache[n]