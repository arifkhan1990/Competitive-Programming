/*                    Name : Aziz Ahmed
                      Judge: HackerEarth
                      problem: Memorise Me!
                      Difficulty: Very Easy
                      Problem Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/memorise-me/
*/


#include <stdio.h>
 
int main() {
	int N, i, query, arr[100000] = {}, temp;
	scanf("%d", &N);
	
	for(i = 0; i < N; i++){
	    scanf("%d", &temp);
	    arr[temp]++;
	}
	
	int Q;
	scanf("%d", &Q);
	
	for(int i = 0; i < Q; i++){
	    scanf("%d", &query);
 
	    if(arr[query] > 0) printf("%d\n", arr[query]);
	    else printf("NOT PRESENT\n");
	}
	return 0;
}