/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 31 - [৫২ সমস্যা বই] যোগ্য সংখ্যা - ২
                      Difficulty: Easy
                      Time Complexity: 0.2536 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/31/perfect-number-2-by-dimik-computing
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	long long ans[] = {6,28,496,8128,33550336};
	long long n, m;
	cin >> n;
	while(n--) {
		cin >> m;
        for(int i = 0; ans[i] <= m; i++) cout << ans[i] << endl;
		if(n != 0)cout << endl;
	}
	return 0;
}