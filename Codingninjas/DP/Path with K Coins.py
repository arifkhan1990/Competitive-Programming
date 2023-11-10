from os import *
from sys import *
from collections import *
from math import *

def solve(grid, k, dp, m, n):
    if m < 0 or n < 0 or k < 0:
        return 0
    elif m == 0 and n == 0:
        return k == grid[m][n]

    dp[m][n][k] = solve(grid, k - grid[m][n], dp, m-1, n) + solve(grid, k - grid[m][n], dp, m, n-1)
    
    return dp[m][n][k]
    
def pathWithKCoins(grid, k) :
    r = grid
    c = grid[0]
    MAX_K = 1000

    dp = [[ [-1 for col in range(MAX_K)]
                for col in range(c)]
                for col in range(r)]
    ans = solve(grid, k, dp, r-1, c-1)

    return ans

    
arr = []

t = int(input())


for i in range(t):
    n , m = map(int, input().split( ))
    x = []
    for j in range(n):
        x = list(map(int, input.strip().split(" ")))
        arr.append(x)
    k = int(input())
    
    print(pathWithKCoins(arr,k))