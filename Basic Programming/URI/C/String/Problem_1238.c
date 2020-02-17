
/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Combiner
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1238
*/


#include <stdio.h>
#include <string.h>

int main(void) {
  int t, i;
  scanf("%d", &t);

  while(t--){
    char s[2][51];
    scanf("%s %s", s[0], s[1]);

    int count = 0;
    for(i = 0; i < (strlen(s[0]) > strlen(s[1]) ? strlen(s[0]) : strlen(s[1])); i++ ){

      if(i >= strlen(s[0])) printf("%c", s[1][i]);
      else if(i >= strlen(s[1])) printf("%c", s[0][i]);
      else {
        printf("%c", s[0][i]);
        printf("%c", s[1][i]);
      }
    }
    printf("\n");
  }
}