from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def minCostToGivenString(str1, str2) :
    if len(str1) < len(str2):
        return -1
    
    cnt , idx1, idx2 = 0, 0, 0

    while idx1 < len(str1) and idx2 < len(str2):
        if str1[idx1] == str2[idx2]:
            idx1, idx2 = idx1 + 1, idx2 + 1
        else:
            cnt += 1
            idx1 += 1
    return cnt


#taking inpit using fast I/O
def takeInput() :
	
    str1 = input().strip()
    str2 = input().strip()
    
    return str1, str2


#main
t = int(input().strip())
for i in range(t) :

    str1, str2 = takeInput()
    print(minCostToGivenString(str1,str2))