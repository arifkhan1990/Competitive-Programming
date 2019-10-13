/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 38 - [৫২ সমস্যা বই] হীরক রাজ্য
                      Difficulty: Easy
                      Time Complexity: 0.2326 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/38/herok-rajjo-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a, b, k;
	cin >> n;
	while(n--) {
	    cin >> a >> b;
	     k = a-1;
	    for(int i = 1; i < a*2; i++) {
	        for(int j = 1; i <= a and j <= i; j++) {
	            if(j != 1) cout << " ";
	            cout << b;
	        }
	        for(int j = 1; i > a and j <= k; j++) {
	            if(j != 1) cout << " ";
	            cout << b;
	        }
	        if(i > a) k--;
	        cout << endl;
	    }
	    cout << endl;
	}
	return 0;
}