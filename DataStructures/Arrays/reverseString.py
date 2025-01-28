string = 'Hi there'

def reverseString(string):
    if (isinstance(string, str)):
        strList = list(string)
        strList.reverse()
        revString = ''.join(strList)
        return revString
    else:
        return "NOT A VALID STRING"

ans = reverseString(string)
print(ans)