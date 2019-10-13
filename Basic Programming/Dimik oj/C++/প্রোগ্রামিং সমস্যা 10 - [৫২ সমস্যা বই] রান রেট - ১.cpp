  
/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 10 - [৫২ সমস্যা বই] রান রেট - ১
                      Difficulty: Easy
                      Time Complexity: 0.1582 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/10/52-problem-book-run-rate-1-by-dimik-computing
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	int n,op_r,bt_r,b,b_played;
	cin >> tc;
	while(tc--){
	cin >> op_r >> bt_r >> b;
	b_played = 300-b;
	double cu_rate = ((bt_r*1.0)/b_played)*6, re_rate = (((op_r + 1 - bt_r )*1.0)/ b )*6;
       if(re_rate < 0.00) re_rate = 0.00;
	printf("%.2lf %.2lf\n",cu_rate,re_rate);
	}
	return 0;
}