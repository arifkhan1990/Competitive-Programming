/*                    Name : Arif Khan
                      Judge: Uri
                      problem: 1069
                      Difficulty: Easy
                      Time Complexity: O(N)
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1069
*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);cin.tie(0);
    int n;
    string s;
    cin >> n;

    while(n--) {
        stack<char>st;
        int ans = 0;
        cin >> s;
        for(auto ch: s) {
            if(ch == '<') st.push(ch);
            else if(!st.empty() and ch == '>') {
                ans++;
                st.pop();
            }
        }
        cout << ans << endl;
    }

    return 0;
}

