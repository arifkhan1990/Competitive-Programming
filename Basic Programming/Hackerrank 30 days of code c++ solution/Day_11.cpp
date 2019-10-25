/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 11: 2D Arrays
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem
*/

#include <bits/stdc++.h>
using namespace std;


int main(){
   // freopen("in.txt","r",stdin);

    int ans = -63,sum = 0,j = 0,d=0,c=0;
    int arr[6][6];
    for(int arr_i = 0;arr_i < 6;arr_i++){
       for(int arr_j = 0;arr_j < 6;arr_j++){
          cin >> arr[arr_i][arr_j];
       }
    }
    for(int i = 0; i < 4; i++){
       for(int i1 = 0 ;i1<4 ;i1++){
            sum = 0;
       for(  j = i; j < i+3; j++,d++){
            for(int p = i1 ;p < i1+3;p++,c++){
                      if(d == 1){
                        if(c == 1)
                            sum += arr[j][p];
                        }else{
                            sum += arr[j][p];
                        }
            }
            c = 0;

       }
        d = 0;
       ans = max(ans,sum);
      }

    }
    cout<<ans<<endl;
    return 0;
}

