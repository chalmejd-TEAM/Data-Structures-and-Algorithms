numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def quickSort(array, left, right):
    if left < right:
        pivot = right
        partitionIndex = partition(array, pivot, left, right)

        quickSort(array, left, partitionIndex -1)
        quickSort(array, partitionIndex+1, right)
    return array

def partition(array, pivot, left, right):
    pivotValue = array[pivot]
    partitionIndex = left

    for i in range(left, right):
        if array[i] < pivotValue:
            swap(array, i, partitionIndex)
            partitionIndex += 1
    swap(array, right, partitionIndex)
    return partitionIndex

def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp

quickSort(numbers, 0, len(numbers)-1)
print(numbers)

