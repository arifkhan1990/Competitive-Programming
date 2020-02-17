
/*                    Name : Aziz Ahmed
                      Judge: URI
                      problem: One-Two-Three
                      Difficulty: Easy 
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1332
*/


#include <stdio.h>
#include <string.h>

int main(void) {
  int t, i;
  scanf("%d", &t);
  while(t--){
    char s[5];
    scanf("%s", s);

    int one_counter = 0, two_counter = 0;
    char one[3] = "one", two[3] = "two";
    if(strlen(s) == 5) printf("3");
    else {
      for(i = 0; i < strlen(s); i++){
        if(s[i] == one[i]) one_counter++;
        if(s[i] == two[i]) two_counter++;
      }

      if(one_counter > two_counter) printf("1");
      else printf("2");
    }
    printf("\n");
  }
}