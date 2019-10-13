#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 23 - [৫২ সমস্যা বই] বর্ণমালা থেকে সংখ্যা
#                      Difficulty: Easy
#                      Time Complexity: 0.4685 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/23/alphabet-to-number-by
#

if __name__ == '__main__':
	
	for _ in range(int(input())):
		a = input()
		for i in a:
			print(ord(i)-65+1,end='')
		print()