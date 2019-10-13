#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 15 - [৫২ সমস্যা বই] অক্ষর গণনা
#                      Difficulty: Easy
#                      Time Complexity: 0.2977 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/15/52-problem-book-counting-characters-by-dimik-computing
#

if __name__ == '__main__':
	n = int(input())
	for i in range(n):
		s = input().strip()
		rs  = sorted(list(set(s)))
		for x in rs:
			cnt = s.count(x)
			print("%c = %d" %(x,cnt))
		if i < n-1:
			print()