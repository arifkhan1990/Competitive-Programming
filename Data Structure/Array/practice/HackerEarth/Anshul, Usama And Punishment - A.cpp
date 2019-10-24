/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Anshul, Usama And Punishment - A
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
#define likeC ios::sync_with_stdio(0); cin.tie(0);

int main()
{
    likeC;
    ll n, ans = 0,ar[21];
    ar[0] = 20, ar[1] = 30;
    cin >> n;
    for(int i = 2; i <= n; i++)
        ar[i] = i%2 ==0? ar[i-2]*2 : ar[i-2]*3;
    sort(ar,ar+n);

    cout << 2*ar[n-1] << endl;
    /* Alternative solution
      ll a = pow(3,((n-2)/2));
      ll b = pow(2, ((n-1)/2));

      cout << (20*b < 30*a ? 60*a : 40*b) << endl;
      */
   return 0;
}

