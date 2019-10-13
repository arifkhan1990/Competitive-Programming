/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 49 - [৫২ সমস্যা বই] মৌলিক কী না
                      Difficulty: Easy
                      Time Complexity: 0.2955 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/49/is-prime-by
*/

#include <bits/stdc++.h>
using namespace std;
#define ll long long int

vector<ll>pr;
void prime_find(ll n)
{
    bool prime[n+1]; 
    memset(prime, true, sizeof(prime)); 
  
    for (ll p=2; p*p<=n; p++) 
    {
        if (prime[p] == true) 
        { 
            for (ll i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    } 
    for (ll p=2; p<=n; p++) 
       if (prime[p]) 
        pr.push_back(p);
}
int main() {
    ll n, p , q, c;
	cin >> n;
	while(n--) {
	    cin >> p;
	    prime_find(sqrt(p));
	    bool is_prime = 1;
	    for(ll i = 0;i < pr.size() and i <= sqrt(p); i++) {
	        if(p % pr[i] == 0){
	            is_prime = 0;
	            break;
	        }
	    }
	    if(is_prime)
	       cout << p << " is a prime" << endl;
	    else
	       cout << p << " is not a prime" << endl;
	   pr.clear();
	}
	return 0;
}