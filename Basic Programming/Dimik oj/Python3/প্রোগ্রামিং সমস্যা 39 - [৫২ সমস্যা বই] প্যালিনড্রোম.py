#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 39 - [৫২ সমস্যা বই] প্যালিনড্রোম
#                      Difficulty: Easy
#                      Time Complexity: 0.4265 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/39/pallidrom-by
#


for _ in range(int(input())):
    s = input()
    s1 = s[::-1]
    print("Yes! It is Palindrome!" if s == s1 else "Sorry! It is not Palindrome!")