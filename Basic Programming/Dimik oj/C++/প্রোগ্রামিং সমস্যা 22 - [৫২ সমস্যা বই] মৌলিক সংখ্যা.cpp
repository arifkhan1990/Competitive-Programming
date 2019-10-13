/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 22 - [৫২ সমস্যা বই] মৌলিক সংখ্যা
                      Difficulty: Easy
                      Time Complexity: 0.2823 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/22/prime-number-by
*/

#include<bits/stdc++.h>
using namespace std;

bool prime[100001];

void primeCheck()
{
	memset(prime, true,sizeof(prime));
	prime[1] = false;prime[0] = false;
	for(int i = 2; i <= sqrt(100001) ; i++) {
		if(prime[i]) {
			for(int j = 2; i*j <= 100001; j++){
				prime[i*j] = false;
			}
		}
	}
}

int main()
{
    int t, a, b;
    scanf("%d",&t);
    primeCheck();
    for(int j = 0; j < t; j++) {
    	cin >> a >> b;
    	int ans = 0;
    	for(int i = a; i <= b; i++) {
    		if(prime[i]) ans++;
    	}
    	cout << ans << endl;
    }
    return 0;
}