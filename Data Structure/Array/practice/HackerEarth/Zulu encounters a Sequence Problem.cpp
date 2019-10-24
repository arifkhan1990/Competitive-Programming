/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Zulu encounters a Sequence Problem
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
    int tc,n;
    cin >> tc;
    while(tc--) {
        cin >>n;
        long long ar[n+1], mx = 0, dif = 0;
        for(int i = 0; i < n; i++) cin >> ar[i];

        for(int i = 0; i < n-1; i++) {
            if(ar[i] >= ar[i+1]) dif+= ar[i]-ar[i+1];
            else mx = max(mx,dif), dif = 0;
            }

            mx = max(mx,dif);dif = 0;

            for(int i = 0; i < n-1; i++) {
                if(ar[i] <= ar[i+1]) dif += ar[i+1]-ar[i];
                else mx = max(mx,dif),dif = 0;
            }
            mx = max(mx,dif),dif = 0;
        cout << mx << endl;
    }

   return 0;
}

