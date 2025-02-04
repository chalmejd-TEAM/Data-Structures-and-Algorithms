numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def mergeSort(array):
    if len(array) <= 1:
        return array
    # Split array into right and left
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


answer = mergeSort(numbers)
print(answer)