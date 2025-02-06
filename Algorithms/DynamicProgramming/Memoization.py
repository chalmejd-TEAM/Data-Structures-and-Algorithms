def addTo80(n):
    return n+80

print(addTo80(5))
print(addTo80(5))
print(addTo80(5))


cache = {}
def memoizedAddTo80(n):
    if n in cache:
        print('Using Cache...')
        return cache[n]
    else:
        print('Adding to Cache...')
        cache[n] = n+80
        return cache[n]

print(memoizedAddTo80(5))
print(memoizedAddTo80(5))
print(memoizedAddTo80(5))