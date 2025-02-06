def addTo80(n):
    return n+80

print(addTo80(5))
print(addTo80(5))
print(addTo80(5))


def memoizedAddTo80():
    cache = {}
    def closure(n):
        nonlocal cache
        if n in cache:
            print('Using Cache...')
            return cache[n]
        else:
            print('Adding to Cache...')
            cache[n] = n+80
            return cache[n]
    return closure

memoized = memoizedAddTo80()

print(memoized(5))
print(memoized(5))
print(memoized(5))
