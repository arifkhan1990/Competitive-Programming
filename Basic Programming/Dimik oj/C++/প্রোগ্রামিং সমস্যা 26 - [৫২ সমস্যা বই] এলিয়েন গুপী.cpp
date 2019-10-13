/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 26 - [৫২ সমস্যা বই] এলিয়েন গুপী
                      Difficulty: Easy
                      Time Complexity: 0.2841 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/26/alien-guppy-by
*/

#include <bits/stdc++.h>
using namespace std;

int gopi(double a)
{
	int ans = 0;
	while(a > 1.0){
		ans++;
		a/=2.0;
	}
	return ans;
}

int main() {
	int tc, b;
	
	cin >> tc;
	
	while(tc--) {
		double a;
		cin >> a;
		cout << gopi(a) << " days" << endl;
	}
	return 0;
}