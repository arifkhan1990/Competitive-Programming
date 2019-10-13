#                      Name : Arif Khan
#                      Judge: Dimik Oj
#                      University: Primeasia University
#                      problem: প্রোগ্রামিং সমস্যা 10 - [৫২ সমস্যা বই] রান রেট - ১
#                      Difficulty: Easy
#                      Time Complexity: 0.2712 সেকেন্ড
#                      Problem Link: https://dimikoj.com/problems/10/52-problem-book-run-rate-1-by-dimik-computing
#
import math
if __name__ == '__main__':
	
	T = int(input())
	data = []
	for i in range(T):
		data = list(map(int, input().split()))
		needRun = data[0] + 1 - data[1]
		lastOver = data[2]/6
		finsedOver = 50 - lastOver
		cur_run_rate = data[1]/finsedOver
		asking_run_rate = needRun/lastOver
        if asking_run_rate < 0.00:
            asking_run_rate = 0.00
		print('%.2lf'%cur_run_rate,'%.2lf'%asking_run_rate,sep=' ')