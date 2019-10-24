/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 6: Let's Review
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-review-loop/problem
*/

#include <bits/stdc++.h>
using namespace std;


int main() {
    string a;
    char b[100000],c[100000];
    int i,n,k,j,l;
    cin>>n;
    while(n>0){
        cin >> a ;
        l = a.size();
        j = k = 0;
        for(i=0;i<l;i++){
            if(i%2==0){
                c[j] = a[i];
                j++;
            }else{
                 b[k] = a[i];
                k++;
            }
            
      
        }
         c[j]='\0';
         b[k]='\0';
        cout<<c<<" "<<b<<endl;
    
        n--;
    }
    return 0;
}

