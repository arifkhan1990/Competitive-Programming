#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 46 - [৫২ সমস্যা বই] ত্রিভুজের ক্ষেত্রফল
#                      Difficulty: Easy
#                      Time Complexity: 0.2489 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/46/area-of-the-triangle-by
#

import math
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    s,area = 0.0, 0.0
    s = float((a+b+c)/2.00)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area = %.3f"%area)