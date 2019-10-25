/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 18: Queues and Stacks
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-queues-stacks/problem
*/

#include <iostream>
#include <stack>
#include <queue>

using namespace std;

class Solution {
    private: 
         queue <char> q;
         stack <char> s;
    public:
         char popCharacter(){
             char temp = s.top();
             s.pop();
             return temp;
         }
    void pushCharacter(char c){
        s.push(c);
    }
        char dequeueCharacter(){
             char temp = q.front();
             q.pop();
             return temp;
         }
    void enqueueCharacter(char c){
        q.push(c);
    }
};

int main() {
    // read the string s.
    string s;
    getline(cin, s);
    
  	// create the Solution class object p.
    Solution obj;
    
    // push/enqueue all the characters of string s to stack.
    for (int i = 0; i < s.length(); i++) {
        obj.pushCharacter(s[i]);
        obj.enqueueCharacter(s[i]);
    }
    
    bool isPalindrome = true;
    
    // pop the top character from stack.
    // dequeue the first character from queue.
    // compare both the characters.
    for (int i = 0; i < s.length() / 2; i++) {
        if (obj.popCharacter() != obj.dequeueCharacter()) {
            isPalindrome = false;
            
            break;
        }
    }
    
    // finally print whether string s is palindrome or not.
    if (isPalindrome) {
        cout << "The word, " << s << ", is a palindrome.";
    } else {
        cout << "The word, " << s << ", is not a palindrome.";
    }
    
    return 0;
}