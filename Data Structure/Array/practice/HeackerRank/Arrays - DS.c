
/*                    Name : Nazrul Islam Rakib
                      Judge: Hacker Rank
                      problem: Arrays - DS 
                      Difficulty: very Easy
                      Time complexity : O(n) 
                      Problem Link: https://www.hackerrank.com/challenges/arrays-ds/problem
*/
#include <stdio.h>

int main(void) {
 
  int i,num;
  scanf("%d" ,&num);
  int arr[num];
  for(i=1 ; i<=num ; i++){
    scanf("%d" , &arr[num-i]);
  }

    for(i=0 ; i<num ; i++){
(i == num-1) ?  printf("%d" , arr[i]) : printf("%d " , arr[i]);
  }

  return 0;
}

