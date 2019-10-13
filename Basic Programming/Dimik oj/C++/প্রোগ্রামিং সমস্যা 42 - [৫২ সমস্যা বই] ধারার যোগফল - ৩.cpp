/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 42 - [৫২ সমস্যা বই] ধারার যোগফল - ৩
                      Difficulty: Easy
                      Time Complexity: 0.3006 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/42/sum-of-the-series-3-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
	cin >> n;
	while(n--) {
	    double sum = 0.0;
	    int x;
	    cin >> x;
	    for(int i = x; i >= 0; i--){
	        if( i > 1) printf("2^%d + ",i);
	        else if(i == 1) printf("%d + ",2);
	        else printf("%d\n",1);
	    }
	}
	return 0;
}