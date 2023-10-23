def sortBinaryArray(arr, n):
    # Write your code here
	c = 0
	for i in arr:
		if i == 0:
			c += 1
	
	for i in range(c):
		arr[i] = 0
	
	for i in range(c, n):
		arr[i] = 1
	
	return arr