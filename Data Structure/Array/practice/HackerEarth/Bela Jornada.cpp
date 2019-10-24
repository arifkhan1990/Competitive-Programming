/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Bela Jornada
               Judge       :   HackerEarth
               Date        :   19/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define likeC ios::sync_with_stdio(0); cin.tie(0);cout.tie(0);

int main()
{
    likeC;
    ll n, a = 0, b = 0,k, mx = 0;
    cin >> n;
    ll ar[n+1],br[n+1];

    for(int i = 0; i < n; i++) {
        cin >> ar[i];
        k += ar[i];
    }
    for(int i = 0; i < n; i++) {
        br[i] = k - ar[i];
        k -= ar[i];
    }
    for(int i = 0; i < n-1; i++) {
        a += ar[i];
        k = br[i]*a;
        mx = max(mx , k);
    }
    cout << mx << endl;
    return 0;
}

