string = 'Hi there'

def reverseString(string):
    if (isinstance(string, str)):
        strList = list(string)
        strList.reverse()
        revString = ''.join(strList)
        return revString
    else:
        return "Not a valid string!"

ans = reverseString(string)
print(ans)