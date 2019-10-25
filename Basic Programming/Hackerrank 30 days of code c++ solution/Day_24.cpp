/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 24: More Linked Lists
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
*/

#include <cstddef>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
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

          Node* removeDuplicates(Node *head)
          {
            Node* curr = head;
            Node* next_next;
            if(curr == NULL) return 0;

            while(c->next != NULL){
                if(curr->data == curr->next->data){
                    next_next = curr->next->next;
                    free(curr->next);
                    c->next = next_next;
                }else{
                    curr = curr->next;
                }
            }
            return head;
          }

          Node* insert(Node *head,int data)
          {
               Node* p=new Node(data);
               if(head==NULL){
                   head=p;  
               }
               else if(head->next==NULL){
                   head->next=p;
               }
               else{
                   Node *start=head;
                   while(start->next!=NULL){
                       start=start->next;
                   }
                   start->next=p;   
               }
                    return head;
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
    head=mylist.removeDuplicates(head);

	mylist.display(head);
		
}