from solution import *
import os
import sys
from copy import deepcopy
sys.setrecursionlimit(10**7)

def beautifulIndex(N: int, A: List[int]) -> int:
    preSum = [0]*(N+1)
    preSum[0] = 0
    for i in range(1,N+1):
        preSum[i] += preSum[i-1] + A[i-1]
    
    for i in range(1,N+1):
        if preSum[i-1] == preSum[-1] - preSum[i]:
            return i
    return -1

class Runner: 
    def __init__(self):
        self.t=0
        self.arr=[]
    def takeInput(self):
        self.t=int(input())
        for l in range(self.t):
            n=int(input())
            #n,m,k=map(int,input().split())
            a=list(map(int,input().split()))
            #b=list(map(int,input().split()))
            #s=input().strip()
            #s1=input().strip()
            self.arr.append([n,a])
    def execute(self):
        arrCopy=deepcopy(self.arr)
        for i in range (self.t):
            ans = beautifulIndex(arrCopy[i][0], arrCopy[i][1])
    
    def executeAndPrintOutput(self):
        for i in range (self.t):
            ans = beautifulIndex(self.arr[i][0], self.arr[i][1])
            print(ans)

runner=Runner()
runner.takeInput()
runner.executeAndPrintOutput()