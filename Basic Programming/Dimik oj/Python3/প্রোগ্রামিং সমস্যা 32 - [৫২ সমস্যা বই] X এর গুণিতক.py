#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 32 - [৫২ সমস্যা বই] X এর গুণিতক
#                      Difficulty: Easy
#                      Time Complexity: 0.3997 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/32/multiplication-of-x-by
#

for _ in range(int(input())):
	n,m = map(int, input().split())
	if n > m:
		print("Invalid!")
	else:
		for i in range(1,m+1):
			if i%n == 0:
				print(i)
	print()