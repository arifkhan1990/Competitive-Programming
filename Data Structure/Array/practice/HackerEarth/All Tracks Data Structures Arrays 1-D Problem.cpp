    /*
                 ...........................................................

                   Solver      :   Arif Khan
                   Problem     :   Mark The Answer
                   Judge       :   HackerEarth
                   Date        :   11/3/19
                   Time        :   O(N)
                   Memory      :   64KB
                   Difficulty  :   Easy

                 ...........................................................
    */
    #include<bits/stdc++.h>
    using namespace std;

    int main()
    {
        long n, m, skip = 1, a, ans = 0, res = 0;
        scanf("%ld %ld",&n,&m);

        while(n--) {
            scanf("%ld",&a);
            if(a <= m) ans++;
            else {
                if(skip) skip = 0;
                else return cout << ans << endl, 0;
            }
        }
        if(skip)
          return cout << ans << endl, 0;
        cout << ans << endl;
        return 0;
    }
