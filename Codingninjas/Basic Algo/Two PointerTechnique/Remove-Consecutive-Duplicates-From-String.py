from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def removeConsecutiveDuplicates(str):
    ans = ""
    l ,  r = 0,1
    while r < len(str):
        if r == len(str) - 1:
            if str[l] == str[r]:
                ans += str[l]
            else:
                ans += str[l] + str[r]
        else:
            if str[l] != str[r]:
                ans += str[l]
        l , r = l+1, r+1
    return ans


# fast input
def takeInput() :
	string = stdin.readline().strip()

	return string
# Main
string = takeInput()
print(removeConsecutiveDuplicates(string))