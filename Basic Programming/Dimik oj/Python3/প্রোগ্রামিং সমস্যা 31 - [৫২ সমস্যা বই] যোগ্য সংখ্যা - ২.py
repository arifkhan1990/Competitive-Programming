#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 31 - [৫২ সমস্যা বই] যোগ্য সংখ্যা - ২
#                      Difficulty: Easy
#                      Time Complexity: 0.3997 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/31/perfect-number-2-by-dimik-computing
#

t = int(input())
ar = [6,28,496,8128,33550336]
for j in range(t):
	n = int(input())
	for i in ar:
		if i <= n:
			print(i)
	if j < t-1:
		print()