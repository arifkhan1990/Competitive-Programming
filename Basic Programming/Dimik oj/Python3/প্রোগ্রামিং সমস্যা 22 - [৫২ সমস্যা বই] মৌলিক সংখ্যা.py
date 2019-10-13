#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 22 - [৫২ সমস্যা বই] মৌলিক সংখ্যা
#                      Difficulty: Easy
#                      Time Complexity: 0.4388 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/22/prime-number-by
#


import math

if __name__ == '__main__':
	prime = [True]*100001
	prime[0] = False
	prime[1] = False
	
	for i in range(2, math.ceil(math.sqrt(100001))):
		if prime[i] == True:
			j = 2
			while i * j < 100001:
				prime[i * j] = False
				j += 1
				
	for _ in range(int(input())):
		a, b = map(int,input().split())
		ans = 0
		for i in range(a,b+1,1):
			if prime[i] == True:
				ans += 1
		print(ans)