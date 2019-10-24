/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 8: Dictionaries and Maps
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
*/

#include <map>
#include <iostream>
using namespace std;


int main() {
    map<string,int>mymap;
  int n,k;
    string name,s_name;
    cin>>n;
    while(n--){
        cin>>name>>k;
        mymap.insert(pair<string,int>(name,k));
    }
    while(cin>>s_name){
        
             if(mymap.count(s_name) != 0)
                 cout<<mymap.find(s_name)->first<<"="<<mymap.find(s_name)->second<<endl;
            else
                 cout<<"Not found"<<endl;
    }
    return 0;
}
