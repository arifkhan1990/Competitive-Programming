if __name__ == '__main__':
	tc = int(input())
	for i in range(1,tc+1):
		k = int(input())
		if k&1:
			print("odd")
		else:
			print("even")