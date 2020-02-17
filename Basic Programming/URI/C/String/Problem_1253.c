
/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: Caesar Cipher
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1253
*/

#include <stdio.h>
#include <string.h>

int main(void) {
  int t, n, i;
  scanf("%d", &t);

  while(t--){
    char s[51];
    scanf("%s", s);
    scanf("%d", &n);

    if(n == 0) printf("%s", s);
    else {
      for(i = 0; i < strlen(s); i++){
        char changed;
        if(s[i] - n < 'A') changed = 'Z' - ('A' - (s[i] - n)) + 1;
        else changed = s[i] - n;
        s[i] = changed;
      }
      printf("%s", s);
    }
    printf("\n");
  }
  return 0;
}