/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 10: Binary Numbers
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
*/


#include <bits/stdc++.h>

using namespace std;
//int *ar = new int[1000001];
vector<int>art;

void tobin(int n1){
    int t;
    while(n1!=0){
        t = n1%2;
        n1/=2;
        art.push_back(t);
    }
}
int main(){
    int n,ans=0,res=0,ans1 = 0;
    cin >> n;
    tobin(n);
    for(int i = art.size()-1; i>=0 ;i--){
        if(art[i] != 1){
          res = max(res,ans);
          ans=0;
        }else{
            ans++;
        }
    }
    res = max(res,ans);
    cout<<res<<endl;
    return 0;
}