#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 27 - [৫২ সমস্যা বই] আর্মস্ট্রং সংখ্যা
#                      Difficulty: Easy
#                      Time Complexity: 0.3060 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/27/armstrong-number-by
#

if __name__ == '__main__':
	
	for _ in range(int(input())):
		a = input()
		b = int(a)
		ans = 0
		for i in a:
			ans += int(i)*int(i)*int(i)
		if ans == b:
			print("{} is an armstrong number!".format(b))
		else:
			print("{} is not an armstrong number!".format(b))