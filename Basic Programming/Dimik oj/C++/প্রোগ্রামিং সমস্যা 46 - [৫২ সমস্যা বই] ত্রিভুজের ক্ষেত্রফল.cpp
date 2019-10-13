/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 46 - [৫২ সমস্যা বই] ত্রিভুজের ক্ষেত্রফল
                      Difficulty: Easy
                      Time Complexity: 0.2893 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/46/area-of-the-triangle-by
*/

#include <bits/stdc++.h>
using namespace std;
#define ll long long int


int main() {
    ll n, p , q, c;
	cin >> n;
	while(n--) {
	    double x, s;
	    cin >> p >> q >> c;
	    s = (p+q+c)/2.00;
	    x = sqrt(s*(s-p)*(s-q)*(s-c));
	    printf("Area = %.3lf\n",x);
	}
	return 0;
}