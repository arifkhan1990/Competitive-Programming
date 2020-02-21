/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Building Houses
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1541
*/

#include <stdio.h>
#include <math.h>

int main(void) {
  while(1){
    int a, b, c;
    scanf("%d", &a);
    if(!a) break;

    scanf("%d %d", &b, &c);

    int ans = pow((double) a*b * ((double)100/c), 0.5); 
    printf("%d\n", ans);

  }
  return 0;
}