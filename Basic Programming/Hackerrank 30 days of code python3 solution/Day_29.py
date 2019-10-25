#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 29: Bitwise AND
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-bitwise-and/problem
#

import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        mx = 0
        f = False
        for i in reversed(range(k)):
            for j in range(10):
                m = 2**j
                if m != (i&m) and (i+m) <= n:
                    mx = i
                    f = True
                    break
            if f:
                break
        
        print(mx)