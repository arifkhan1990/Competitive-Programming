#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 50 - [৫২ সমস্যা বই] লেফট-রাইট
#                      Difficulty: Easy
#                      Time Complexity: 0.3128 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/50/left-right-by
#

for _ in range(int(input())):
    s = input()
    r = ''
    for i in range(len(s)):
        if s[i] in 'L':
            r +=s[i-1]
        elif s[i] in 'R':
            r +=s[i+1]
        else:
            r +=s[i]
    print(r)