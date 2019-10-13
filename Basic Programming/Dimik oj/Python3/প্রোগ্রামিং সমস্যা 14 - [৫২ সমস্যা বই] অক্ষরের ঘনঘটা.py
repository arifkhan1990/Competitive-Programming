#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 14 - [৫২ সমস্যা বই] অক্ষরের ঘনঘটা
#                      Difficulty: Easy
#                      Time Complexity: 0.4021 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/14/52-problem-book-cumulus-characters-by-dimik-computing
#

if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		s = input()
		ch = input()
		ans = s.count(ch)
		if ans > 0:
			print("Occurrence of '%c' in '%s' = %d" %(ch,s,ans))
		else:
			print("'%c' is not present"% ch)