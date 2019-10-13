/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 27 - [৫২ সমস্যা বই] আর্মস্ট্রং সংখ্যা
                      Difficulty: Easy
                      Time Complexity: 0.4935 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/27/armstrong-number-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	
	int ar[11];
	ar[0] = 0;
	for(int i = 1; i < 10; i++){
  	ar[i] = i*i*i;
	}
	
	int tc, b;
	
	cin >> tc;
	
	while(tc--) {
		int a,sum = 0, re = 0, b;
		cin >> a;
		b = a;
		while(a != 0) {
			re = a%10;
			a /= 10;
			sum += ar[re];
		}
		if(b == sum)
		   cout << b << " is an armstrong number!" << endl;
		else
		   cout << b << " is not an armstrong number!" << endl;
	}
	return 0;
}