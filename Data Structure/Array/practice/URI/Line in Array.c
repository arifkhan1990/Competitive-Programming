
/*                    Name : Nazrul Islam Rakib
                      Judge: URI
                      problem: Line in Array 
                      Difficulty: very Easy
                      Time complexity : O(n*n) 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1181
*/

#include <stdio.h>

int main(void) {
 
  char ch;
  int i,j,lineNo;
  float ar[12][12],count = 0.0;

  scanf("%d " , &lineNo);
  scanf("%c", &ch);

  for ( i=0 ; i<12; i++){
    for( j=0 ; j<12 ; j++){     

      scanf("%f" , &ar[i][j]);

      if( i == lineNo){
        count += ar[i][j];
      }
    }
  }

  if(ch == 'S'){
    printf("%0.1f\n" , count);
  }else{
     printf("%0.1f\n" , count/12.0);
  }

  return 0;
}

