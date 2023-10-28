
def maximumFrequency(arr, n):
	mx = 0
	ans = 0
	a = {}

	for i in arr:
		if i not in a:
			a[i] = 1
		else:
			a[i] += 1

	for i in arr:
		if mx < a[i]:
			mx = a[i]
			ans = i
	return ans