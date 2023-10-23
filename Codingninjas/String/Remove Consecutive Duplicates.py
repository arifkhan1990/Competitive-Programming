
def solve(i,n,s, ans):
	if i == n-1:
		ans.append(s[n-1:])
		return ans
	if s[i] != s[i+1]:
		ans.append(s[i])
	solve(i+1, n, s, ans)
	
def removeDuplicate(n, s):
	ans = []
	solve(0,n,s,ans)
	return "".join(ans)