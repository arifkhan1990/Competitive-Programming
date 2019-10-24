#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 9: Recursion 3
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-recursion/problem
#

import sys

def factorial(n):
    if(n<=1):
        return 1
    else:
        return factorial(n-1)*n

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)