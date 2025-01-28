string = 'Hi my name is Jacob'

def reverseString(str):
    strList = list(str)
    strList.reverse()
    revString = ''.join(strList)
    return revString

ans = reverseString(string)
print(ans)