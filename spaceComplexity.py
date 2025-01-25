def boo(n):
    for i in range(len(n)):
        print('boo')

boo([1,2,3,4,5]) # Space complexity of O(1)

def arrayHiNTimes(n):
    hiArray = []
    for i in range(n):
        hiArray = hiArray + ['hi']
    return hiArray

x = arrayHiNTimes(6) # Space complexity of O(n)
print(x)