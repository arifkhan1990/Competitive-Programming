#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 42 - [৫২ সমস্যা বই] ধারার যোগফল - ৩
#                      Difficulty: Easy
#                      Time Complexity: 0.5878 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/42/sum-of-the-series-3-by
#

for _ in range(int(input())):
    x = int(input())
    for i in range(x,-1,-1):
        if i > 1:
            print("2^{} + ".format(i),end='')
        elif i == 1:
            print("{} + ".format(2),end='')
        else:
            print(1)