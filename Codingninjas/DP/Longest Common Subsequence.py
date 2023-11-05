from copy import deepcopy
from solution import getLengthOfLCS
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
import os

def lcs(X,Y,m,n):
    ans = [[None]*(n+1) for i in range(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                ans[i][j] = 0
            elif X[i-1] == Y[j-1]:
                ans[i][j] = ans[i-1][j-1]+1
            else:
                ans[i][j] = max(ans[i-1][j], ans[i][j-1])
    return ans[m][n]
    
def getLengthOfLCS(str1, str2):
    m = len(str1)
    n = len(str2)
    return lcs(str1, str2, m, n)

class Runner:
    def __init__(self):
        self.t = 0
        self.arr = []
        self.arr2 = []
        
    def takeInput(self):
        self.t = int(input().strip())
        for i in range(self.t):
            a, b = input().split(" ")
            
            self.arr.append(a)
            self.arr2.append(b)

    def getCopy(self):
        arrCopy, arr2Copy = deepcopy(self.arr), deepcopy(self.arr2)
        return arrCopy, arr2Copy
    
    def executeAndPrintOutput(self):
        for i in range(self.t):
            ans = getLengthOfLCS(self.arr[i], self.arr2[i])
            print(ans)
        
    def execute(self):
        arrCopy, arr2Copy = self.getCopy()
        for i in range(self.t):
            ans = getLengthOfLCS(arrCopy[i], arr2Copy[i])



runner = Runner()
runner.takeInput()
runner.executeAndPrintOutput()
