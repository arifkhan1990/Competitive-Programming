#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 24 - [৫২ সমস্যা বই] একান্তর উপাদান
#                      Difficulty: Easy
#                      Time Complexity: 0.2388 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/24/alternate-elements-by
#

if __name__ == '__main__':
	
	for _ in range(int(input())):
		a = int(input())
		ar = list(map(int, input().split()))
		for i in range(0,a,2):
			if i == 0:
				print("%d"%ar[i],end='')
			else:
				print(" %d"%ar[i],end='')
		print()