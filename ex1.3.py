def func(n, cache=[1, 1]):
    if n < len(cache):
        return cache[n]
    else:
        new_val = func(n-1) + func(n-2)
        cache.append(new_val)
        return new_val