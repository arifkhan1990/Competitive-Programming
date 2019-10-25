/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 16: Exceptions - String to Integer
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
*/

#include <iostream>
using namespace std;

int main(){
    string S;
    cin >> S; 
    
    try{
        int  t = stoi(S);
        cout<<t<<endl;
    }catch( exception e){
        cout <<"Bad String"<<endl;
    }    
    return 0;
}
