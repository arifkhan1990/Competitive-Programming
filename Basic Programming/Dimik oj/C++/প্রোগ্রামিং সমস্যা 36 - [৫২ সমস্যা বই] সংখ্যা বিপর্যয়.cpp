/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 36 - [৫২ সমস্যা বই] সংখ্যা বিপর্যয়
                      Difficulty: Easy
                      Time Complexity: 0.3937 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/36/number-disaster-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
	cin >> n;
	while(n--) {
	    long num, ren, de, reverseNum = 0;
	    cin >> num;
	    while(num != 0) {
	        ren = num%10;
	        num /= 10;
	        reverseNum = reverseNum*10 + ren;
	    }
	    cout << reverseNum << endl;
	}
	return 0;
}