#                      Name : Arif Khan
#                      Judge: URI
#                      University: Primeasia University
#                      problem: Encrypted Christmas Letter
#                      Difficulty: Easy
#                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/3038
# 

import sys;  
s=sys.stdin.read()
ans  = s
for i in s:
	if i in "@&!*#":
		if i == '@':
			ans = ans.replace('@','a')
		elif i == '&':
			ans = ans.replace('&','e')
		elif i == '!':
			ans = ans.replace('!','i')
		elif i == '*':
			ans = ans.replace('*','o')
		elif i == '#':
			ans = ans.replace('#','u')
print(ans)
