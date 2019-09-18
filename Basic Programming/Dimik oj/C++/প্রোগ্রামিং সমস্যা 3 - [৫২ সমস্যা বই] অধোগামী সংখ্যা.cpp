#include<bits/stdc++.h>
using namespace std;

int main()
{

    for(int i = 1000,j = 1; i > 0; i--, j++) {
      printf("%d\t",i);
      if(j == 5){
          cout << endl;
          j = 0;
      }
    }
    return 0;
}