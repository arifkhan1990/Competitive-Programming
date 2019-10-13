#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 72 - ত্রিভুজ (ISCPC 2018 Preliminary)
#                      Difficulty: Easy
#                      Time Complexity: 0.5223 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/72/iscpc-2018-preliminary-b
#

import math
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    s,area = 0.0, 0.0
    if ((a+b) < c or (b+c) < a or (a+c) < b):
        print("Oh, No!")
    else:
        s = float((a+b+c)/2.00)
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("%.2f"%area)