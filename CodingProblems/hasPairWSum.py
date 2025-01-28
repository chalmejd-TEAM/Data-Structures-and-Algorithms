array1 = [1,2,3,9]
array2 = [1,2,4,4]
array3 = [1,6,4,9,2,3,4,5,6,7,1,5,4,3,9,4]
array4 = []
array5 = [1]*100000

sum = 9

def hasPairWSum(array, sum):
    comp = []
    for value in range(len(array)):
        if array[value] in comp:
            return True
        comp.append(sum-array[value])
    return False

ans = hasPairWSum(array5, sum)
print(ans)