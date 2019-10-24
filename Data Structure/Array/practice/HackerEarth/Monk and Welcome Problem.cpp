/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Monk and Welcome Problem
               Judge       :   HackerEarth
               Date        :   3/9/18
               Time        :   O(N)
               Memory      :   1072KB
               Difficulty  :   Very-Easy

             ...........................................................
*/
    #include<bits/stdc++.h>
    using namespace std;

    int main()
    {
        long long t,n,k;
        cin >> n;
         long ar[n+1];
            for(int i = 0; i < n; i ++)
               {
                 cin >> ar[i];
               }
             for(int i = 0; i < n; i ++)
               {
                 cin >> k;
                 cout << ar[i]+k << " ";
               }
               cout << endl;

        return 0;
    }
