/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 11 - [৫২ সমস্যা বই] গৌণিক / ফ্যাক্টরিয়াল
                      Difficulty: Easy
                      Time Complexity: 0.1800 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/11/52-problem-book-factorial-by-dimik-computing
*/

#include <iostream>
using namespace std;

long long int fact(int n)
{
	if(n  <= 1) return 1;
	return n * fact(n-1);
}

int main() {
	int n, t;
	cin >> n;
	while(n--) {
		cin >> t;
		cout << fact(t) << endl;
	}
	return 0;
}