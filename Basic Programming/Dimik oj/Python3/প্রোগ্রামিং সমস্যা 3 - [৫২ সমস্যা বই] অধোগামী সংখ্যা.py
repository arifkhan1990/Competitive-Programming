if __name__ =="__main__":
	j = 0
	for i in range(1000,0,-1):
		print(i,end='\t')
		j += 1
		if j == 5:
			print()
			j = 0