#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 30 - [৫২ সমস্যা বই] যোগ্য সংখ্যা - ১
#                      Difficulty: Easy
#                      Time Complexity: 0.4734 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/30/perfect-number-1-by-dimik-computing
#


import math
for _ in range(int(input())):
	ar = int(input())
	sum, lp = 1, int(math.sqrt(ar))
	for i in range(2,lp+1):
		if ar%i == 0:
			sum += i + (ar//i)
		if sum > ar:
		    break
	if sum == ar:
		print("YES, {} is a perfect number!".format(ar))
	else:
		print("NO, {} is not a perfect number!".format(ar))