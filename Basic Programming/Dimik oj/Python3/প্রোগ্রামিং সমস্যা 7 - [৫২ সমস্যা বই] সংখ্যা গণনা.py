if __name__ == '__main__':
	tc = int(input())
	for i in range(1,tc+1):
		num = 0;
		k = []
		k = map(int, input().split())
		for i in k:
			num += 1
		print(num)