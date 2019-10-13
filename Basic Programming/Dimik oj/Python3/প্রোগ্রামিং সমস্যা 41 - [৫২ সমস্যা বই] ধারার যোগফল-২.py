#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 41 - [৫২ সমস্যা বই] ধারার যোগফল-২
#                      Difficulty: Easy
#                      Time Complexity: 0.6055 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/41/sum-of-the-series-2-by
#

def fac(n):
    p = 1
    for i in range(1,n+1):
        p *= i
    return p
    
for _ in range(int(input())):
    x = int(input())
    sum = 0.0
    for i in range(1,x+1):
        sum += (float(i)/fac(i))
    print("%.4f"%(sum))