#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 12 - [৫২ সমস্যা বই] ফ্যাক্টরিয়াল 100
#                      Difficulty: Easy
#                      Time Complexity: 0.4945 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/12/52-problem-book-factorial-100-by-dimik-computing
#

import math
if __name__ == '__main__':
	tc = int(input())
	for i in range(tc):
		k = int(input())
		ans = 0
		while k > 0:
			ans += k//5
			k //= 5
		print(ans)