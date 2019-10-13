/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 15 - [৫২ সমস্যা বই] অক্ষর গণনা
                      Difficulty: Easy
                      Time Complexity: 0.1727 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/15/52-problem-book-counting-characters-by-dimik-computing
*/

#include <iostream>
using namespace std;

int main() {
	int t;
	string s;
	cin >> t;
	while(t--) {
	    int ar[256]= {0};
		cin >> s;
		for(char ch : s){
			ar[ch]++;
		}
		
		for(char ch = 'a' ; ch <= 'z';ch++ ) {
			if(ar[ch] > 0) cout << ch  << " = " << ar[ch] << endl;
		}
		if(t>=1)cout << endl;
	}
	return 0;
}