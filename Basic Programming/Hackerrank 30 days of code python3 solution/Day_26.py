#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 26: Nested Logic
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-nested-logic/problem
#

d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

ans = 0
if y1 > y2:
    ans = 10000
elif y1 == y2:
    if m1 > m2:
        ans = (m1-m2)*500
    elif m1==m2 and d1 > d2:
        ans = (d1-d2)*15
print(ans)