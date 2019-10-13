/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 32 - [৫২ সমস্যা বই] X এর গুণিতক
                      Difficulty: Easy
                      Time Complexity: 0.4519 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/32/multiplication-of-x-by
*/

#include <bits/stdc++.h>
using namespace std;
 
int main() {
	long long n, y, x;
	cin >> n;
	while(n--) {
		long long m = 1;
		cin >> x >> y;
        if(x > y) cout << "Invalid!" << endl;
        else{
        	while(m*x <= y) {
        		cout << m*x << endl;
        		m++;
        	}
        }
            cout << endl;
	}
	return 0;
}