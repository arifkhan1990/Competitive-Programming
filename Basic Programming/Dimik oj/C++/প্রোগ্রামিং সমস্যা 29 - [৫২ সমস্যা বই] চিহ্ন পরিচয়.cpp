/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 29 - [৫২ সমস্যা বই] চিহ্ন পরিচয়
                      Difficulty: Easy
                      Time Complexity: 0.2779 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/29/symbol-identity-by
*/

#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	
	while(n--) {
		char ch;
		cin >> ch;
		if(ch >= 'a' and ch <= 'z') cout << "Lowercase Character" << endl;
		else if(ch >= 'A' and ch <= 'Z') cout << "Uppercase Character" << endl;
		else if(ch >= '0' and ch <= '9') cout << "Numerical Digit" << endl;
		else cout << "Special Character" << endl;
	}
	return 0;
}