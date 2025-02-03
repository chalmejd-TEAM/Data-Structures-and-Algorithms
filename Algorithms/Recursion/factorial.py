
# O(n)
def findFactorialRecursive(number):
    if number == 2:
        return 2
    return number * findFactorialRecursive(number-1)  

# O(n)
def findFactorialIterative(number):
    answer = 1
    if number == 2:
        answer = 2
    for i in range(2,number+1):
        answer = answer*i
    return answer

ansIter =findFactorialIterative(5)
ansRec = findFactorialRecursive(10)

print('Iterative Answer:', ansIter)
print('Recursive Answer:', ansRec)