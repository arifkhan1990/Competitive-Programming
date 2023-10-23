



def firstNonRepeatingCharacter(str):

    a = {}
    for i in str:
        if i not in a:
            a[i] = 1
        else:
            a[i] = 0

    for i in str:
        if a[i] == 1:
            return i
    return str[0]
    
