#include<iostream>
using namespace std;

int front = 0, rear = 0; 

void enqueue(int queue[], int element, int arrSize)
{
    if(rear != arrSize){
        queue[rear] = element;
        rear++;
    }
}

void dequeue(int queue[])
{
    if(front != rear){
        queue[front] = 0;
        front++;
    }
}

int frontData(int queue[])
{
    return queue[front];
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
    int n, k;
    cin >> n;
    int queue[n+1];
    for(int i = 0; i < n; i++){
        cin >> k;
        enqueue(queue, k, n);
    }
    cout << "Queue size : " << size() << endl;
    cout << "Queue first element = " << frontData(queue) << endl;
    dequeue(queue);
    cout << "Queue new first element = " << frontData(queue) << endl;
    cout << "Queue is empty = " << (isEmpty()? "True":"False") << endl;
    cout << "Queue data are : " ;
    while(!isEmpty()) {
        cout << frontData(queue) << " ";
        dequeue(queue);
    }
    cout << endl;
    cout << "Queue is empty = " << (isEmpty()? "True":"False") << endl;
    return 0;
}