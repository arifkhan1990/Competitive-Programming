#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 18 - [৫২ সমস্যা বই] স্বরবর্ণ-ব্যাঞ্জনবর্ণ
#                      Difficulty: Easy
#                      Time Complexity: 0.3734 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/18/52-problem-book-vowels-and-consonants-by-dimik-computing
#

for _ in range(int(input())):
	s = input()
	v = "AEIOUaeiou"
	vowelWord = ""
	conWord = ""
	for x in s:
		if x in v:
			vowelWord += x
		elif ((x >= 'A' and x <= 'Z') or (x >= 'a' and x <= 'z')):
			conWord += x
	
	print(vowelWord)
	print(conWord)