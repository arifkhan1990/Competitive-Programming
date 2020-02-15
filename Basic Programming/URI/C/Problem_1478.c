/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Square Matrix II
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1478
*/

#include <stdio.h>

int main(void) {

  while (1) {
    int input;
    scanf("%d", & input);
    if (!input) break;
    int data[input][input];

    int i, j, k;
    for (i = 0; i < input; i++) {
      for (j = 0; j < input - i; j++) {
        data[i][j + i] = j + 1;
      }
      for (j = 0; j < input - i; j++) {
        data[j + i][i] = j + 1;
      }
    }

    for (i = 0; i < input; i++) {
      for (j = 0; j < input; j++) {
        int count = 0;
        int temp = data[i][j];
        while (temp != 0) {
          count++;
          temp /= 10;
        }

        for (k = count; k < 3; k++) {
          printf(" ");
        }

        printf("%d", data[i][j]);
        if (j != input - 1) printf(" ");
      }
      printf("\n");
    }
    printf("\n");
  }

  return 0;
}