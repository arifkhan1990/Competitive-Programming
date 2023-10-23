def emptyCells(N, K, tasks):
	# pass all test case 5/5
	r = c = N
	rMat = set()
	cMat= set()
	res = []
	for k in tasks:
		if k[0] not in rMat:
			rMat.add(k[0])
			r -= 1
		
		if k[1] not in cMat:
			cMat.add(k[1])
			c -= 1
			
		res.append(r*c)
		
	return res
	# TLE test case pass 3/5
	# mat = []
	# for i in range(N):
	# 	x = []
	# 	for j in range(N):
	# 		x.append(None)
	# 	mat.append(x)
	# ans = 0
    
	# res = []
	# for k in tasks:
	# 	for i in range(N):
	# 		if mat[k[0]][i] != 0:
	# 			mat[k[0]][i] = 0
	# 			ans += 1

	# 	for i in range(N):
	# 		if mat[i][k[1]] != 0:
	# 			mat[i][k[1]] = 0
	# 			ans += 1
	# 	res.append(N*N - ans)
		
	# return res

test_cases = int(input())

while test_cases:

	N, K = map(int, input().split())
	tasks = []

	for t in range(K):
		i,j = map(int,input().split())
		X = i,j
		tasks.append(X)

	output = emptyCells(N, K, tasks)

	for emptyCell in output:
		print(emptyCell, end=' ')

	print()
	test_cases -= 1