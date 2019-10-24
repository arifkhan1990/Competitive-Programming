/*
             ...........................................................

               Solver      :   Arif Khan
               Problem     :   Monk and Power of Time
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
    int n, a, ans = 0;
    scanf("%d",&n);
    deque<int> calling, order;
    for(int i = 0; i < n; i++) {
        cin >> a;
        calling.push_back(a);
    }
    for(int i = 0; i < n; i++) {
        cin >> a;
        order.push_back(a);
    }

    while(!calling.empty() and !order.empty()) {
        if(order.front() == calling.front()) {
            order.pop_front();
            calling.pop_front();
        }else{
            calling.push_back(calling.front());
            calling.pop_front();
        }
        ans++;
    }
    cout << ans << endl;
    return 0;
}
