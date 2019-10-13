/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 28 - [৫২ সমস্যা বই] এলোমেলো অ্যারে
                      Difficulty: Easy
                      Time Complexity: 0.2840 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/28/random-array-by
*/

#include <iostream>
using namespace std;

int main() {
	int ac = 1,dc = 1,n, k , ar[101];
	cin >> n;
	for(int i = 0; i < n; i++) cin >> ar[i];
	
	for(int i = 0; i < n - 1; i++) {
		if(ar[i] > ar[i+1]) ac = 0;
		if(ar[i] < ar[i+1]) dc = 0;
	}
	
	cout << ((ac or dc)? "YES":"NO") << endl;
	return 0;
}