/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Dedication Level = Infinity
               Judge       :   HackerEarth
               Date        :   15/3/19
               Time        :   O(N)
               Memory      :   64KB
               Difficulty  :   Easy

             ...........................................................
*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, ti, i = 0;
    string name;
    scanf("%d",&n);
    multimap<int,string, greater<int>> data;
    multimap<int,string>:: iterator it;
    while(n--) {
        cin >> name;
        scanf("%d",&ti);
        data.insert(make_pair(ti,name));
    }
    for(it = data.begin(); it != data.end() and i++ < 3; it++) {
        printf("%d\n", it->second);
    }
    return 0;
}
