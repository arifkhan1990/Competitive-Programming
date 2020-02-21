/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Roman Numerals for Page Numbers
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1960
*/


#include <stdio.h>

int main(void) {
  int num, i, j;
  int fact[] = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
  char fact_char[13][3] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};

  scanf("%d", &num);
  for(i = 12; i >= 0; i--){
    int d = num / fact[i];
    num %= fact[i];

    for(j = 0; j < d; j++){
      printf("%s", fact_char[i]);
    }
    
  }

  printf("\n");

  return 0;
}