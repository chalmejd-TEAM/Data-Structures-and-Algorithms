# Given 2 arrays, create a function that lets the user know (true/false) whether the two arrays contain any common items.
# For example:
# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'i']
# should return False
# --------
# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'x']
# should return True

# Inputs/Outputs:
# 2 parameters - arrays - no size limit
# return True/False

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']

#-----------------------------------------------------
# Brute force: nested for loops O(n*m)

def checkCommonItems(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                return True
    return False

ans = checkCommonItems(array1, array2)
print(ans)

#------------------------------------------------------
# Less time complexity: consecutive for loops O(n+m)

# array1 ==> dic {
#     a: True,
#     b: True,
#     c: True,
#     x: True
# }
# array2[index] == dic.key

def checkCommonItems2(array1, array2):
    # Loop through first array and create dictionary and create object where keys = items in the array
    # Loop through second array and check if item in second array exists in created dictionary

    arrayDict = {}
    
    for i in range(len(array1)):
        arrayDict[array1[i]] = True

    for j in range(len(array2)):
        if array2[j] in arrayDict:
            return True
        
    return False


ans2 = checkCommonItems2(array1, array2)
print(ans2)