# Given an array, return the first recurring character of the array
# array = [2,5,1,2,3,5,1,2,4]
# should return 2

# array = [2,1,1,2,3,5,1,2,4]
# should return 1

# array = [2,3,4,5]
# should return undefined

def firstRecurring(array):
    holder = {}
    for i in range(len(array)):
        if array[i] in holder:
            return array[i]
        else:
            holder[array[i]] = i

ans = firstRecurring([2,3,4,5])
print(ans)
