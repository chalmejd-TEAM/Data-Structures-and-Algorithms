# Given a number N, return the index value of the Fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# Each value is the sum of the 2 previous values

# O(n)
def fibonacciIterative(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]

# O(2^n): Exponential time - BAD!
def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

# O(n)
def fibonacciRecDynamic():
    cache = {}
    def fib(n):
        nonlocal cache
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n-1)+fib(n-2)
                return cache[n]
    return fib

ansRec = fibonacciRecursive(11)
print('Recursive Answer:', ansRec)

ansIter = fibonacciIterative(120)
print('Iterative Answer:', ansIter)

fibDyn = fibonacciRecDynamic()
print('Dynamic Answer:', fibDyn(120))
