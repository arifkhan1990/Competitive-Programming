/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Pepper and Contiguous Even Subarray
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
        int tc, n , m;
        scanf("%d",&tc);
        while(tc--) {
            scanf("%d",&n);
            vector<int> subArray;
            int ans = -1;
            for(int i = 0; i < n ; i++) {
                    cin >> m;
                    if(m%2 == 0) {
                        subArray.push_back(m);
                    }else {
                        int p = (subArray.size() > 0) ? subArray.size() : -1;
                        ans = max(ans, p);
                        subArray.clear();
                    }
            }
            int p = (subArray.size() > 0) ? subArray.size() : -1 ;
            ans = max(ans, p);
            cout << ans << endl;
        }
        return 0;
    }
