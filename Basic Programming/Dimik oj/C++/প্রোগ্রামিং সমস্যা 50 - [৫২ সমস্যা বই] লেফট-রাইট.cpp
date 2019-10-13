/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 50 - [৫২ সমস্যা বই] লেফট-রাইট
                      Difficulty: Easy
                      Time Complexity: 0.3268 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/50/left-right-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
	cin >> n;
	while(n--) {
	    string s, s1;
	    cin >> s;
	    for(int i = 0; i < s.size(); i++) {
	        if( s[i] == 'L') s1 += s[i-1];
	        else if(s[i] == 'R') s1 += s[i+1];
	        else s1 += s[i];
	    }
	    cout << s1 << endl;
	}
	return 0;
}