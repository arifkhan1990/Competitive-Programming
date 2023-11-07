
def slidingWindowMaximum(nums:list, k:int):
	ans = []
	n = len(nums)
	for i in range(n-k+1):
		x = max(nums[i: i+k])
		ans.append(x)
	return ans