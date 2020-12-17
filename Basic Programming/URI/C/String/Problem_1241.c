
/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Fit or Dont Fit II
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1241
*/


#include <stdio.h>
#include <string.h>

int main(void) {
  int t, i;
  scanf("%d", &t);
  while(t--){
    char s1[1001], s2[1001];
    scanf("%s %s", s1, s2);

    if(strlen(s1) < strlen(s2)) printf("nao encaixa");
    else {
      int counter = 0;
      for(i = 0; i < strlen(s2); i++){
        if(s1[strlen(s1) - strlen(s2) + i] == s2[i]) counter++;
        else break;
      }

      if(counter == strlen(s2)) printf("encaixa");
      else printf("nao encaixa");
    }
    
    printf("\n");
  }
}