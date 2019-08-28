#include<iostream>
#include<queue>
using namespace std;

int main()
{
    int n, m, k;
    cin >> n;
    queue<int>q;
    while(n--) {
        cin >> m;
        q.push(m);
    }

    cout << "Queue size :" << q.size() << endl;
    cout << "Queue Front element : " << q.front() << endl;
    cout << "Queue Back element : " << q.back() << endl;
    cout << "Remove first element in queue : ";
     q.pop();
    while(!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }

    cout << "\nCheck Queue is Empty or not" << endl;

    if(q.empty()) {
        cout << "\t\tSTL queue are provide more operation :" << endl;
        cout << "\t\t\tq.emplace()\n\t\t\tq1.swap(q2)" << endl;
    }

    return 0;
}