/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Fredo and Large Numbers
               Judge       :   HackerEarth
               Date        :   12/3/19
               Time        :   O(N*N)
               Memory      :   64KB
               Difficulty  :   Medium

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    int n;
    map<ll, ll> mp, mp1;
    vector<ll> v;
    ll ans[1000005],res[1000005];
    scanf("%d",&n);
    ll ar[n+5];

    for(int i = 0; i < n; i++) {
        scanf("%lld",&ar[i]);
        if(mp[ar[i]] == 0) v.push_back(ar[i]);
        mp[ar[i]]++;
    }
    ans[0] = 0;
    ll j = 1;
    for(ll i = 0, sz = v.size(); i < sz; i++) {
        ll p = mp[v[i]];
        for(; j <= p ; j++) {
            ans[j] = v[i];
        }
        if(mp1[p] == 0) res[p] = v[i];
        mp1[p]++;
    }
    ll mx = -1;
    for(ll i = 0; i < n; i++) mx = max(mx,mp[ar[i]]);

    int q;
    scanf("%d",&q);
    while(q--) {
        ll a, b;
        scanf("%lld %lld",&a,&b);
        if(b > mx) printf("0\n");
        else cout << (a? res[b]:ans[b]) << endl;

    }
    return 0;
}

