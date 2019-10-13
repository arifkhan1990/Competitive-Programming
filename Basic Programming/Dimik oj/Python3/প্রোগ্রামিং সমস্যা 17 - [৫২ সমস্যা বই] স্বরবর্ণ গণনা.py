#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 17 - [৫২ সমস্যা বই] স্বরবর্ণ গণনা
#                      Difficulty: Easy
#                      Time Complexity: 0.3608 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/17/52-problem-book-counting-vowels-by-dimik-computing


for _ in range(int(input())):
	s = input()
	v = "AEIOUaeiou";
	cnt = 0;
	
	for x in s:
		if x in v:
			cnt += 1
	print("Number of vowels = %d"%cnt)