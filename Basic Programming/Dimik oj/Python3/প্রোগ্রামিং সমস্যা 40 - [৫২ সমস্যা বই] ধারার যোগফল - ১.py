#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 40 - [৫২ সমস্যা বই] ধারার যোগফল - ১
#                      Difficulty: Easy
#                      Time Complexity: 0.2881 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/40/sum-of-the-series-1-by
#

for _ in range(int(input())):
    x, y = map(int, input().split())
    sum, p = 1, 1
    for i in range(1,y+1):
        p *= x
        sum += p
    print("Result = {}".format(sum))