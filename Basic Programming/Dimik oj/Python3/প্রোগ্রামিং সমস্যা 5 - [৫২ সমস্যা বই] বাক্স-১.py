if __name__ == '__main__':
	tc = int(input())
	for i in range(1,tc+1):
		k = int(input())
		for j in range(1,k+1):
			for p in range(1,k+1):
				print('*',end='')
			print()
		if i != tc:
			print()