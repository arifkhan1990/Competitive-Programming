/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 41 - [৫২ সমস্যা বই] ধারার যোগফল-২
                      Difficulty: Easy
                      Time Complexity: 0.2683 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/41/sum-of-the-series-2-by
*/

#include <bits/stdc++.h>
using namespace std;
#define ll long long int

ll fact(ll n){
    ll i , p = 1;
    for(i = 1; i <= n; i++) p *= i;
    return p;
}

int main() {
    int n;
	cin >> n;
	while(n--) {
	    double sum = 0.0;
	    ll x;
	    cin >> x;
	    for(ll i = 1; i <= x; i++){
	        sum += (double(i)/fact(i));
	    }
	    printf("%.4lf\n",sum);
	}
	return 0;
}