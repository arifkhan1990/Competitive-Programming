import os
import sys
sys.setrecursionlimit(10**7)
from solution import maxAreaContainer

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    ans = maxAreaContainer(arr)
    print(ans)


class Runner:
    def __init__(self):
        self.arr = []
        self.t = 0

    def takeInput(self):
        self.t = int(input())
        for c in range(self.t):
            n = int(input())
            temp = list(map(int, stdin.readline().strip().split(" ")))
            self.arr.append(temp)

    def getCopy(self):
        arrCopy = deepcopy(self.arr)
        return arrCopy

    def execute(self):
        arrCopy = self.getCopy()
        for i in range(self.t):
            maxAreaContainer(arrCopy[i])

    def executeAndPrintOutput(self):
        for i in range(self.t):
            ans = maxAreaContainer(self.arr[i])
            print(ans)


runner = Runner()
runner.takeInput()
runner.executeAndPrintOutput()