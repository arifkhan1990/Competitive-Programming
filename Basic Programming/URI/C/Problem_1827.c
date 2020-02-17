/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Square Array IV
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1827
*/

#include <stdio.h>

int main(void) {
  int input, i, j;
  while(scanf("%d", &input) !=  EOF){
    for(i = 0; i < input; i++){
      for(j = 0; j < input; j++){
        if(i < input/3 || i >= input - (input/3)){
          if(i == j) printf("2");
          else if(i+j == input-1) printf("3");
          else printf("0");
        } else {
          if(i == input/2 && j == input/2) printf("4");
          else if(j < input/3 || j >= input - (input/3)) printf("0");
          else printf("1");
        }
      }
      printf("\n");
    }
    printf("\n");
  }
}