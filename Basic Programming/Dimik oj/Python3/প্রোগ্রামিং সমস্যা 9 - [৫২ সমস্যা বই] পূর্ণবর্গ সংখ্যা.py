#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 9 - [৫২ সমস্যা বই] পূর্ণবর্গ সংখ্যা
#                      Difficulty: Easy
#                      Time Complexity: 0.3006 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/9/52-problem-book-perfect-squares-by-dimik-computing
#


import math
if __name__ == '__main__':
	tc = int(input())
	for i in range(0,tc):
		n = int(input())
		d = int(math.sqrt(n))
		print('YES' if d*d == n else 'NO')