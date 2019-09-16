if __name__ == '__main__':
	tc = int(input())
	for i in range(1,tc+1):
		k = int(input())
		print("Case ",end='')
		print(i,end='')
		print(':',end=' ')
		for j in range(1,(k//2)+1):
			if not k%j:
				print(j,end=' ')
		print(k)