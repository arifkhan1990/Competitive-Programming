
from sys import stdin


def getMaximumProfit(values, n) :
	#Your code goes here
    ans = 0
    res = 0
    for i in range(n-1):
        if values[i+1] >= values[i]:
            ans += values[i+1] - values[i]
       
    return ans




#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    values = list(map(int, stdin.readline().rstrip().split(" ")))
    return values, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    values, n = takeInput()
    print(getMaximumProfit(values, n))
    t -= 1
