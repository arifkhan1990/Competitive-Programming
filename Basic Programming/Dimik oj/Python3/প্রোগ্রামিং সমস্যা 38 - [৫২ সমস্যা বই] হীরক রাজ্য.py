#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 38 - [৫২ সমস্যা বই] হীরক রাজ্য
#                      Difficulty: Easy
#                      Time Complexity: 0.3333 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/38/herok-rajjo-by
#

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(1, a+1):
        print(*[b]*i)
    for i in range(a-1, 0, -1):
        print(*[b]*i)
    print()