if __name__ == '__main__':
	tc = int(input())
	for i in range(1,tc+1):
		k = input()
		if int(k[-1])&1:
			print("odd")
		else:
			print("even")