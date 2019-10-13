#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 33 - [৫২ সমস্যা বই] বিভাজনসাধ্য-১
#                      Difficulty: Easy
#                      Time Complexity: 0.2721 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/33/division-1-by
#

for _ in range(int(input())):
	n,m,p = map(int, input().split())
	while n%p:
		n += 1
	for i in range(n,m+1,p):
		if i%p == 0:
			print(i)
	print()