#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 25 - [৫২ সমস্যা বই] লঘিষ্ঠ সাধারণ গুণিতক
#                      Difficulty: Easy
#                      Time Complexity: 0.6154 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/25/longer-common-multiples-by
#


def gcd(a,b):
	if b == 0:
		return a
	return gcd(b, a%b)

if __name__ == '__main__':
	
	for _ in range(int(input())):
		a,b = list(map(int, input().split()))
		print("LCM = ",end='')
		print((a*b)//gcd(a,b))