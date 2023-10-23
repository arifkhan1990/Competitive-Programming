from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def getMinimumAnagramDifference(str1, str2):
    ans1, ans2 = 0, 0
    a = Counter(str1)
    b = Counter(str2)
    # print(a)
    # print(b)
    for i in str2:
        if i in a:
            a[i] -= 1
    for i in str1:
        if i in b:
            b[i] -= 1
    # print(a)
    # print(b)
    for i in set(str1):
        if a[i] > 0:
            ans1 += a[i]
    for i in set(str2):
        if b[i] > 0:
            ans2 += b[i]
    # print(ans1, ans2)
    return max(ans1, ans2)


# Taking Input.
def takeInput():
    str1 = stdin.readline().strip()
    str2 = stdin.readline().strip()
    return str1, str2

# Main.
T = int(stdin.readline().strip())
for i in range(T):
    str1, str2 = takeInput()
    ans = getMinimumAnagramDifference(str1, str2)
    print(ans)