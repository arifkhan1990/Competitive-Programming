/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 15: Linked List
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-linked-list/problem
*/

#include <iostream>
#include <cstddef>
using namespace std;

class Node
{
    public:
        int data;
        Node *next;
        Node(int d){
            data=d;
            next=NULL;
        }
};
class Solution{
    public:

      Node* insert(Node *head,int data)
      {
          Node* newNode = new Node(data);
          Node * tail = head;

          if(!head)
             return newNode;
          for(;tail->next; tail = tail->next);
          tail->next = newNode;

          retur head;
      }

      void display(Node *head)
      {
          Node *start=head;
          while(start)
          {
              cout<<start->data<<" ";
              start=start->next;
          }
      }
};

int main()
{
	Node* head=NULL;
  	Solution mylist;
    int T,data;
    cin>>T;
    while(T-->0){
        cin>>data;
        head=mylist.insert(head,data);
    }	
	mylist.display(head);
		
}