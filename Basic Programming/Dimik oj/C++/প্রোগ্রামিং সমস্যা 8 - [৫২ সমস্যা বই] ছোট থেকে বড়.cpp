/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 8 - [৫২ সমস্যা বই] ছোট থেকে বড়
                      Difficulty: Easy
                      Time Complexity: 0.1504 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/8/52-problem-book-smaller-to-larger-by-dimik-computing
*/
#include <bits/stdc++.h>
using namespace std;
 
int main() {
	int n;
	int ar[3];
	cin >> n;
	for(int i = 1; i <= n; i++) {
		printf("Case %d: ",i);
		cin >> ar[0] >> ar[1] >> ar[2];
        sort(ar,ar+3);
        cout << ar[0] << " " << ar[1] << " " << ar[2] << endl;
	}
	return 0;
}