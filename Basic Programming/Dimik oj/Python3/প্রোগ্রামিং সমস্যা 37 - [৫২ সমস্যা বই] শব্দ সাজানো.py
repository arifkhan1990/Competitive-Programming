#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 37 - [৫২ সমস্যা বই] শব্দ সাজানো
#                      Difficulty: Easy
#                      Time Complexity: 0.3506 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/37/word-sorting-by
#

ar = []
for i in range(int(input())):
    s = input()
    ar.append(s)
d = sorted(ar)
for i  in d:
    print(i)