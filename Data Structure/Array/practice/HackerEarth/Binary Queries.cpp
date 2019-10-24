/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Binary Queries
               Judge       :   HackerEarth
               Date        :   3/9/18
               Time        :   O(N*N)
               Memory      :   4196KB
               Difficulty  :   Very-Easy

             ...........................................................
*/
    #include<bits/stdc++.h>
    using namespace std;

    int scan(){
        	register int c = getchar_unlocked();
            int n = 0;
            for( ; (c<48 || c>57); c = getchar_unlocked() );
            for( ; (c>47 && c<58); c = getchar_unlocked() ){
                n = (n<<1) + (n<<3) +c -48;
            }
            return n;
    }
    void scan1(){
        	register int c = getchar_unlocked();
            for( ; (c<48 || c>57); c = getchar_unlocked() );
            for( ; (c>47 && c<58); c = getchar_unlocked() );
    }

    int main()
    {
        int n, m,b = 1, dec = 0, k , l,s,e;
        n = scan();
        m = scan();
        int biar[n+1];
        for(int i = 1; i <= n; i++)  biar[i] = scan();
        while(m--){
            b = 1, dec = 0,
            cin >> k;
            if(k == 1){
                 l = scan();
                biar[l] = biar[l] != 0 ? 0 : 1;
            }else{
                scan1();
                e = scan();
                cout << (biar[e] == 1 ? "ODD":"EVEN") << endl;
            }
        }
        return 0;
    }
