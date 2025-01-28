# Merge two sorted arrays into one large sorted array:

array1 = [1,2,3,4,5,6,7,8,"a"]
array2 = [1,2,3,"z",5,6]

def mergeSortedArrays(array1, array2):
    if (isinstance(array1, list) & isinstance(array2, list)):
        array1.extend(array2)
        sortedArray = sortMixed(array1)
        return sortedArray
    else:
        return "Not valid arrays"

# Handle arrays of mixed ints and strs
def sortMixed(array):
    integerSort = sorted([i for i in array if type(i) is int])
    mixedSort = sorted([j for j in array if type(j) is str])
    return integerSort+mixedSort

ans = mergeSortedArrays(array1, array2)
print(ans)