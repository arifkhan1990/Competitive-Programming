#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 35 - [৫২ সমস্যা বই] বৃত্তের বাইরে
#                      Difficulty: Easy
#                      Time Complexity: 0.3301 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/35/out-of-the-circle-by
#

import math
if __name__ == '__main__':
  t = int(input())
  for j in range(t):
    x1,y1 = map(float, input().split())
    r = float(input())
    x2,y2 = map(float, input().split())
    dis = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    print("The point is not inside the circle" if dis > r else "The point is inside the circle")