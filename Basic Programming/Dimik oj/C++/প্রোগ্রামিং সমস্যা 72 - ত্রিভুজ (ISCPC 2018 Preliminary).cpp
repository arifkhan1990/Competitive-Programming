/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 72 - ত্রিভুজ (ISCPC 2018 Preliminary)
                      Difficulty: Easy
                      Time Complexity: 0.3238 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/72/iscpc-2018-preliminary-b
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
	    if((p+q) < c or (q+c) < p or (c+p) < q){
	          cout << "Oh, No!" << endl;
	    }else{
	      	  s = (p+q+c)/2.00;
	          x = sqrt(s*(s-p)*(s-q)*(s-c));
	          printf("%.2lf\n",x);
	    }
	}
	return 0;
}