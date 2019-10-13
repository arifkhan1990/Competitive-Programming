/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 30 - [৫২ সমস্যা বই] যোগ্য সংখ্যা - ১
                      Difficulty: Easy
                      Time Complexity: 0.4912 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/30/perfect-number-1-by-dimik-computing
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	
	while(n--) {
		int m, sum = 0;
		cin >> m;
		for(int i = 1; i <= m/2 and sum < m; i++) {
			if(m%i == 0) sum += i;
		}
	    if(sum == m) printf("YES, %d is a perfect number!\n", m);
	    else printf("NO, %d is not a perfect number!\n", m);
	}
	return 0;
}