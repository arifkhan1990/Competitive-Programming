#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen('in.txt','r',stdin);
    string s;
    int b = 1;
    cin >> s;

    stack<char>st;

    for(char x: s) {
        if(x == ')') {
            if(st.top() == '(') st.pop();
            else {
                b = 0;
                break;
            }
        }else if(x == '}') {
            if(st.top() == '{') st.pop();
            else {
                b = 0;
                break;
            }
        }else if(x == ']') {
            if(st.top() == '[') st.pop();
            else {
                b = 0;
                break;
            }
        }else {
            st.push(x);
        }
    }

    cout << ((st.empty() and b)? "Yes" : "No") << endl;
    return 0;
}
