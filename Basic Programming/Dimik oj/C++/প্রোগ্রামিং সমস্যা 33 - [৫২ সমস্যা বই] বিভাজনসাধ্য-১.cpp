/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 33 - [৫২ সমস্যা বই] বিভাজনসাধ্য-১
                      Difficulty: Easy
                      Time Complexity: 0.5408 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/33/division-1-by
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
long long n, y, x, z;
	scanf("%lld",&n);
	while(n--) {
		scanf("%lld %lld %lld", &x, &y, &z);
        for(long long i = x; i <= y;) {
            if(i%z == 0) { printf("%lld\n", i), i+=z;}
            else i++;
        }
      printf("\n");
	}
	return 0;
}