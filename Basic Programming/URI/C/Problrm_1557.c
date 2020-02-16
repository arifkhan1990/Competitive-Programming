/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Square Matrix III
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1557
*/

#include <stdio.h>

#include <math.h>

int numberlength(int number);

int
numberLength(int number) {

  int count = 0;

  while (number != 0) {

    count++;

    number /= 10;

  }

  return count;

}

int
main(void) {

  while (1) {

    int input, i, j, k;

    scanf("%d", & input);

    if (!input)
      break;

    int max_num = pow(2, input-1) * pow(2, input-1);

    int max_align = numberLength(max_num);

    for (i = 0; i < input; i++) {

      for (j = 0; j < input; j++) {

        int num = pow(2, i) * pow(2, j);

        //align
        for (k = numberLength(num); k < max_align; k++) {

          printf(" ");

        }

        printf("%d", num);

        if (j != input - 1)
          printf(" ");

      }

      printf("\n");

    }
    printf("\n");

  }
  

  return 0;

}