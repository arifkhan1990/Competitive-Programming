#include<iostream>
#include<stack>
using namespace std;

int main()
{
    int n, m;
    stack<int>st;

    cin >> n;
    while(n--) {
        cin >> m;
        st.push(m); // insert data in stack
    }

    int sz = st.size(); // stack size

    cout << "Size of Stack : " << sz << endl;

    cout << "Print Stack Data : " ;

    while(!st.empty()) {
        cout << st.top() << " ";
        st.pop();
    }

    cout << endl;

    return 0;
}
