/*                    Name : Arif Khan , Asif Khan, Ripon Ahammed , Munna, Subho, Hossain Ahammed
                      Judge: HackerRank
                      problem: Sets-STL
                      Difficulty: Easy
                      Time Complexity: O(N)
                      Problem Link: https://www.hackerrank.com/challenges/cpp-sets/problem
*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int numberOfQuery, queryType, value;

    set<int>st;

    cin >> numberOfQuery;
    while(numberOfQuery--) {
        cin >> queryType >> value;

        if(queryType == 1) {
            st.insert(value);
        }else if(queryType == 2) {
            st.erase(value);
        }else {
            cout << (st.count(value)? "Yes":"No") << endl;
        }
    }
    return 0;
}
