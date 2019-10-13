#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: পপ্রোগ্রামিং সমস্যা 26 - [৫২ সমস্যা বই] এলিয়েন গুপী
#                      Difficulty: Easy
#                      Time Complexity: 0.3034 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/26/alien-guppy-by
#


if __name__ == '__main__':
	
	for _ in range(int(input())):
		a = float(input())
		ans = 0
		while a > 1.0:
			ans += 1
			a /= 2.0
		print("{} days".format(ans))