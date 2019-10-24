/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   B) Team Selection
               Judge       :   HackerEarth
               Date        :   15/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ll n, ans = 0, lp;
    scanf("%lld",&n);
    ll res[n+1];
    vector<ll> ar,br;
    for(int i = 0; i < n; i++) {scanf("%lld",&lp); ar.push_back(lp);}
    for(int i = 0; i < n; i++) {scanf("%lld",&lp); br.push_back(lp);}

    sort(br.begin(),br.end());
    for(int i = 1; i < n; i++) {
        ll p = upper_bound(br.begin(),br.end(),ar[i]) - br.begin();
        res[i] = (p!=n)? n-p : 0;
    }
    for(int i = 0; i < n; i++) {
        for(int k = i+1; k < n; k++) {
            if(ar[i] < ar[k]) ans += res[k];
       }
    }
    cout << ans << endl;
    return 0;
}

