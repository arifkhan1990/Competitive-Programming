/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Battlefield (MEDIUM)
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
   int tc, n;
   string s;
   cin >> tc;
   while(tc--) {
    int k = 0, mx = 0, ans = 0;
    cin >> n >> s;
    for(auto x : s) if (x == 'K') k++;

    for(int i = 0; i < k; i++) if(s[i] == 'K') ans++;

    for(int i = 0; i < n; i++) {
        if(s[(i+k)%n] == 'K') ans++;
        if(s[i] == 'K') ans--;
        mx = max(mx,ans);
    }
    cout << mx  << endl;
   }

   return 0;
}
