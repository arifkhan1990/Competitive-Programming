/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Help Jarvis
               Judge       :   HackerEarth
               Date        :   3/9/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/

    #include<bits/stdc++.h>
    using namespace std;

    int main()
    {
        int n;
        string s;
        cin >> n;
        while(n--) {
            cin >> s;
            sort(s.begin(),s.end());
            int b = 1;
            for(int i = 0; i < s.size() - 1; i ++) {
                if(s[i]+1 != s[i+1]) {
                    cout << "NO\n";
                    b = 0;
                    break;
                }
            }
            if(b) cout << "YES\n";
        }
        return 0;
    }
