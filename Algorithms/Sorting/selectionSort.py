numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array):
    for i in range(len(array)):
        currentLow = i
        for j in range(i, len(array)):
            if array[currentLow] > array[j]:
                currentLow = j
        array[i], array[currentLow] = array[currentLow], array[i]
    return

selectionSort(numbers)
print(numbers)