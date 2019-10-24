/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Anshul, Usama And Punishment - B
               Judge       :   HackerEarth
               Date        :   11/3/19
               Time        :   O(N*N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;


int main()
{

    unsigned long long n, ans = 0;
    cin >> n;
    unsigned long long ar[63];
    ar[0] = 20, ar[1] = 30;
    for(int i = 2; i <= n; i++) {
        ar[i] = (i%2 == 0)? ar[i-2]*2 : ar[i-2]*3 ;
    }

    sort(ar,ar+n);
    cout << 2*ar[n-1] << endl;
    return 0;
}
