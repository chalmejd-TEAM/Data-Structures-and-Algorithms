x = [1,2,3,4,5]

def logAllPairs(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                print(array[i], array[j])   

logAllPairs(x)