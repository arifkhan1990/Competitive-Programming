#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 8 - [৫২ সমস্যা বই] ছোট থেকে বড়
#                      Difficulty: Easy
#                      Time Complexity: 0.2385 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/8/52-problem-book-smaller-to-larger-by-dimik-computing
#


if __name__ == '__main__':
	tc = int(input())
	a = [3]
	
	for i in range(1, tc+1):
		print('Case ',i,': ',sep='',end='')
		#a = list(map(int, input().split()))
		#a.sort()
		a = sorted(map(int, input().split()))
		print(*a, sep = " ")