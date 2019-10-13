#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 29 - [৫২ সমস্যা বই] চিহ্ন পরিচয়
#                      Difficulty: Easy
#                      Time Complexity: 0.3788 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/29/symbol-identity-by
#


if __name__ == '__main__':
	for _ in range(int(input())):
		ch = input()
		
		if ch >= 'a' and ch <= 'z':
			print("Lowercase Character")
		elif ch >= 'A' and ch <= 'Z':
			print("Uppercase Character")
		elif ch >= '0' and ch <= '9':
			print("Numerical Digit")
		else:
			print("Special Character")