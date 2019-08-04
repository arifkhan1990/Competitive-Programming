#include<bits/stdc++.h>
using namespace std;

int stk[10001];
int top = -1;

void push(int data, int n)
{
    if(top != n-1) {
        stk[++top] = data;
    }
}

bool empty()
{
    return (top == -1)? 1:0;
}

void pop()
{
    if(!empty()) top--;
}

int size()
{
    return top+1;
}

int topData()
{
    return stk[top];
}

int main()
{
    int n,m;
    cin >> n;

    for(int i =0; i < n; i++) {
        cin >> m;
        push(m,n);
    }

    cout << "Size of Stack :  " << size() << endl;
    while(!empty()) {
        cout << topData() << " ";
        pop();
    }
    cout << endl;
    return 0;
}
