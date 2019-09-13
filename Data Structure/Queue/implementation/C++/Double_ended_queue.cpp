#include<iostream>
using namespace std;

int queue[1001], front = 0, rear = 0;

void enqueueBack(int element, int n)
{
    if(rear != n) {
        queue[rear] = element;
        rear++;
    }
}

void enqueueFront(int element, int n) 
{
    if(rear != n) {
        for(int i = rear; i > front; i--) {
            queue[i] = queue[i-1];
        }
        queue[front] = element;
        rear++;
    }
}

void dequeueBack()
{
    if(front != rear) {
        queue[--rear] = 0;
    }
}

void dequeueFront()
{
    if(front != rear){
        queue[front++] = 0;
    }
}

int get_front()
{
    return queue[front];
}

int get_back()
{
    return queue[rear-1];
}

int size()
{
    return rear - front;
}

bool isEmpty()
{
    return front == rear;
}

int main()
{
    int n, k, m;
    cin >> n >> m;

    for(int i = 0; i < n; i++) {
       cin >> k;
       enqueueFront(k, n);
    }
    cout << "Queue element are :";
        for(int i = 0; i < n; i++) cout << queue[i] << " ";
    cout << endl;

    for(int i = 0; i < m; i++) {
       cin >> k;
       enqueueBack(k,n+m);
    }

    cout << "Queue element are :";
        for(int i = 0; i < n+m ; i++) cout << queue[i] << " ";
    cout << endl;
    
    cout <<"Queue size :" << size() << endl;
    cout << "Queue is empty = " << (isEmpty()? "True":"False") << endl;
    
    cout << "Queue front element = " << get_front() << endl;
    cout << "Queue back element = " << get_back() << endl;
    dequeueFront();
    dequeueBack();
    cout << "Queue new front element = " << get_front() << endl;
    cout << "Queue new back element = " << get_back() << endl;
    cout <<"Queue new size :" << size() << endl;
    return 0;
}
