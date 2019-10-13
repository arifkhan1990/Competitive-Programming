#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 16 - [৫২ সমস্যা বই] শব্দ বিপর্যয়
#                      Difficulty: Easy
#                      Time Complexity: 0.2230 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/16/52-problem-book-reverse-words-by-dimik-computing


if __name__ == '__main__':
	test = int(input())
	for i in range(test):
		sentence = input().split(' ')
		res = []
		for x in sentence:
			word = "".join(reversed(x)) 
			res.append(word)  #res.append(x[::-1])
		print(' '.join(res))