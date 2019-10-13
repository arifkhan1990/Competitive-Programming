/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 39 - [৫২ সমস্যা বই] প্যালিনড্রোম
                      Difficulty: Easy
                      Time Complexity: 0.4537 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/39/pallidrom-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
	cin >> n;
	while(n--) {
	    string s, s1;
	    cin >> s;
	    
	    s1 = s;
	    reverse(s1.begin(),s1.end());
	    cout << ((s == s1)? "Yes! It is Palindrome!":"Sorry! It is not Palindrome!") << endl;
	}
	return 0;
}