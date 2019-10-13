#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 34 - [৫২ সমস্যা বই] বিভাজনসাধ্য-২
#                      Difficulty: Easy
#                      Time Complexity: 0.5496 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/34/division-2-by
#

def gcd(x, y):
  if y == 0:
    return x
  return gcd(y, x%y)

if __name__ == '__main__':
  t = int(input())
  for j in range(t):
    n,m,p = map(int, input().split())
    lcm = int((n*m)/gcd(n,m))
    for i in range(lcm,p,lcm):
      print(i)
    if j < t-1:
      print()