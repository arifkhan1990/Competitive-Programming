/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Array 123
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1534
*/

#include <stdio.h>

int main(void) {
  int input, i, j;
  while(scanf("%d", &input) != EOF){
    for(i = 0; i < input; i++){
      for(j = 0; j < input; j++){
        if(i+j == input-1) printf("2");
        else if(i == j) printf("1");
        else printf("3");
      }
      printf("\n");
    }
  }
  return 0;
}