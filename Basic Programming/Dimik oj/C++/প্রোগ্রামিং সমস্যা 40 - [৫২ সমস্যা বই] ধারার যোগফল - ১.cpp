/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 40 - [৫২ সমস্যা বই] ধারার যোগফল - ১
                      Difficulty: Easy
                      Time Complexity: 0.3892 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/40/sum-of-the-series-1-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x , y;
	cin >> n;
	while(n--) {
	    int sum = 1, p = 1;
	    cin >> x >> y;
	    for(int i = 1; i <= y; i++){
	        p *= x;
	        sum += p;
	    }
	    cout << "Result = " << sum << endl;
	}
	return 0;
}