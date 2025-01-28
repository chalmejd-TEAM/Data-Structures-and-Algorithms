nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = nemo * 100000

def findNemo(array):
    count = 0
    for i in range(len(array)):
        if(array[i] == 'nemo'):
            count = count + 1
    print(count, 'Nemos found')
    
findNemo(large)  # O(n) ---> Linear Time

def logFirstTwo(array):
    print(array[0])
    print(array[1])

logFirstTwo(everyone) #O(1) ---> Constant Time