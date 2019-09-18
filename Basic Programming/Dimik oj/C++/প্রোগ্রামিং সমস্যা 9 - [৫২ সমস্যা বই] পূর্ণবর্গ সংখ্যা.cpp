/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 9 - [৫২ সমস্যা বই] পূর্ণবর্গ সংখ্যা
                      Difficulty: Easy
                      Time Complexity: 0.2222 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/9/52-problem-book-perfect-squares-by-dimik-computing
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
	long n,tc;
	cin >> tc;
	while(tc--){
	cin >> n;
	long int d = sqrt(n);
	if(d*d == n) cout << "YES" << endl;
	else cout << "NO" << endl;
	}
	return 0;
}