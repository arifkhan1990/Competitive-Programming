/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Testing Strings
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
const ll mod = 1e6 + 3;
int main()
{
    ll n, m, k, l,r,z,ans = 1;
    cin >> n >> m >> k;
    vector<int> a[m+1], b[m+1];
    while(n--) {
        cin >> l >> r >> z;
        a[l].push_back(z);
        b[r].push_back(z);
    }

    map<int, int>letter;
    for(int i = 1; i <= m; i++) {
        for(int j = 0; j < a[i].size(); j++) letter[a[i][j]]++;
        ans = (ans * (k-letter.size()))  % mod;
        for(int j = 0; j < b[i].size(); j++) {
            letter[b[i][j]]--;
            if(letter[b[i][j]] <= 0) letter.erase(b[i][j]);
        }
    }
    cout << ans << endl;
    return 0;
}
