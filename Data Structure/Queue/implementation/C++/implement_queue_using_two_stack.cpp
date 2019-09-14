#include<iostream>
#include<stack>
using namespace std;

stack<int> s1, s2;

void enqueue(int data)
{
    while(!s1.empty()) {
        s2.push(s1.top());
        s1.pop();
    }
    s1.push(data);

    while(!s2.empty()) {
        s1.push(s2.top());
        s2.pop();
    }
}

void dequeue()
{
    if(!s1.empty()) {
        s1.pop();
    }
}

int front()
{
    return s1.top();
}

bool isEmpty()
{
    return s1.size() == 0;
}

int size()
{
    return s1.size();
}

void printData()
{
    while(!s1.empty()) {
        cout << s1.top() << " ";
        s1.pop();
    }
    cout << endl;
}

int main()
{
    int n, m, k;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> k;
        enqueue(k);
    }

    cout << "Queue is empty : " << (isEmpty()?"True":"False") << endl;
    cout << "Queue front element : " << front() << endl;
    dequeue();
    cout << "Queue size : " << size() << endl;
    enqueue(12);
    enqueue(6);
    cout << "Queue new size : " << size() << endl;
    cout << "Queue new element are : ";
     printData();
    cout << "Queue is empty : " << (isEmpty()?"True":"False") << endl;
    return 0;
}