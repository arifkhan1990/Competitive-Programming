
/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Square Matrix I
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1435
*/

#include <stdio.h>

int main(void) {
  int input;
  while(1){
    scanf("%d",&input);
    if(!input) break;
    int i, j, k;
    for(i = 1; i <= input; i++){
      int min_i = i <= input-i ? i : input - i + 1;
      for(j = 1; j <= input; j++){
        int min_j = j <= input-j ? j : input - j + 1;
        int min = min_i <= min_j ? min_i : min_j;
        
        //digit count
        int temp = min;
        int count = 0;
        while(temp != 0){
          count++;
          temp /= 10;
        }

        for(k = count; k < 3; k++){
          printf(" ");
        }

        printf("%d", min);
        if(j != input) printf(" ");
        
      }
      printf("\n");
    }
    printf("\n");
  }
  return 0;
}