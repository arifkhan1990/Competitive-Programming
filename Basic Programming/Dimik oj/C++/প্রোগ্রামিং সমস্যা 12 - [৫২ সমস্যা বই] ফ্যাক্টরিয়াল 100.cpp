/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 12 - [৫২ সমস্যা বই] ফ্যাক্টরিয়াল 100
                      Difficulty: Easy
                      Time Complexity: 0.1271 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/12/52-problem-book-factorial-100-by-dimik-computing
*/

#include <iostream>
using namespace std;


int main() {
	int n, t;
	cin >> n;
	while(n--) {
		cin >> t;
		int ans = 0;
		while(t > 0) {
			ans += t/5;
			t/=5;
		}
		cout << ans << endl;
	}
	return 0;
}