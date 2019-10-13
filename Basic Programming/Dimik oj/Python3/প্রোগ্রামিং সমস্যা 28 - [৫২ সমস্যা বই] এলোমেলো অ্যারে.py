#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 28 - [৫২ সমস্যা বই] এলোমেলো অ্যারে
#                      Difficulty: Easy
#                      Time Complexity: 0.3087 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/28/random-array-by
#


if __name__ == '__main__':
	n = int(input())
	ar = []
	for _ in range(n):
		ar.append(int(input()))

	ac =  1
	for i in range(1,n):
		if ar[i-1] > ar[i]:
			ac = 0
	print("YES" if ac else "NO")