/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 34 - [৫২ সমস্যা বই] বিভাজনসাধ্য-২
                      Difficulty: Easy
                      Time Complexity: 0.2979 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/34/division-2-by
*/

#include <bits/stdc++.h>
using namespace std;
 
long long gcd(long long x, long long y)
{
	if(y == 0) return x;
	return gcd(y, x%y);
}
 
int main() {
long long n, y, x, z;
	cin >> n;
	while(n--) {
		cin >> x >> y >> z;
		long long lcm = x*y/gcd(x,y);
        for(int i = lcm; i <= z; i+=lcm) {
            cout << i << endl;
        }
      if(n != 0) cout << endl;
	}
	return 0;
}