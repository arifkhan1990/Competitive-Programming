/*                    Name : Nazrul Islam Rakib
                      Judge: URI online judge
                      problem: Array Hash
                      Difficulty: Easy
                      Time Complexity: O(N*M) ba O(N>M or M>N)
                      Problem Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1257
*/


#include <stdio.h>
#include <string.h>

int main(void) {

  int i,j, mainCount ;
  int numberOfIteration=0 , numberOfQuery=0;  // Initializing the variables
  char str[200];

  scanf("%d",&numberOfIteration);
 
  while(numberOfIteration--){           // take input how long the process will run

    mainCount = 0;

     scanf("%d",&numberOfQuery);        // take input how many query have to execute 

     for(i = 0; i<numberOfQuery ; i++){

      scanf("%s", str);                 // take input the string
      int length = strlen(str);

      for(j=0 ; j < length ; j++){

        int alphabetPosition = str[j]-65;    // find out alphabet position 

        mainCount += (alphabetPosition + j + i);     // i = element , j= position 
      }

    }

    printf("%d\n" , mainCount);
  }
  return 0;
}