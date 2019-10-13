/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 25 - [৫২ সমস্যা বই] লঘিষ্ঠ সাধারণ গুণিতক
                      Difficulty: Easy
                      Time Complexity: 0.2861 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/25/longer-common-multiples-by
*/

#include <bits/stdc++.h>
using namespace std;

int gcd(long long a, long long b)
{
	if(b == 0) return a;
	return gcd(b, a%b);
}
int main() {
	long long tc, a, b;
	
	cin >> tc;
	
	while(tc--) {
		cin >> a >> b;
		
		cout << "LCM = " <<  (a*b)/gcd(a,b) << endl;
	}
	return 0;
}