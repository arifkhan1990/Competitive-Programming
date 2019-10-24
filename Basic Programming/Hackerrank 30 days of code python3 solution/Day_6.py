#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 6: Let's Review
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-review-loop/problem
#


n = int(input())
while n != 0:
    s = input()
    w1, w2 = "", ""
    for i in range(0, len(s)):
        if i%2:
            w2 += s[i]
        else:
            w1 += s[i]
    print("{} {}".format(w1, w2))
    n -= 1