/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 14 - [৫২ সমস্যা বই] অক্ষরের ঘনঘটা
                      Difficulty: Easy
                      Time Complexity: 0.1800 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/14/52-problem-book-cumulus-characters-by-dimik-computing
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	string s;
	char ch;
	scanf("%d ",&t);
	while(t--) {
		getline(cin , s);
		scanf("%c ",&ch);

		size_t n = count(s.begin(), s.end(), ch);
		if(n > 0){
			cout << "Occurrence of " << "'" << ch <<"'" << " in '" << s << "' = " << n << endl;
		}else {
			cout << "'" << ch << "' is not present" << endl;
		}
	}
	return 0;
}