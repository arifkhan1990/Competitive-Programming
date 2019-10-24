/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   The Amazing Race
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
const ll mod = 1e9 + 7;

int main()
{
    likeC;
   ll tc, n , m, x, y, sum = 0;
   scanf("%lld",&tc);
   while(tc--) {
    cin >> n;
    stack<ll> high, low;
    ll ar[n+1], frontData[n+1],backData[n+1];
    for(int i = 1; i <= n ; i++) {
            cin >> ar[i];
    }
    backData[1] = 0;
    high.push(1);
    for(int i = 2; i <= n ; i++) {
            while(!high.empty() and ar[i] > ar[high.top()]) high.pop();

            if(!high.empty()) backData[i] = i - high.top();
            else backData[i] = i - 1;

            high.push(i);
    }

    frontData[n] = 0;
    low.push(n);
    for(int i = n -1;i >= 1; i--) {
        while(!low.empty() and ar[i] > ar[low.top()]) low.pop();
        if(!low.empty()) frontData[i] = low.top() - i;
        else frontData[i] = n - i;

        low.push(i);
    }
    ll mx = -1;
    int idx = -1;

    for(int i = 1; i <= n ; i++) {
        ll sum = backData[i] + frontData[i];
        sum = ((sum % mod) * i)%mod;

        if(sum > mx) {
            mx = sum;
            idx = i;
        }
    }
    cout << idx << endl;
   }

   return 0;
}

