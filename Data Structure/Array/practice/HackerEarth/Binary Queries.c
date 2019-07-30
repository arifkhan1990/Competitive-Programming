/*                    Name : Aziz Ahmed
                      Judge: HackerEarth
                      problem: Binary Queries
                      Difficulty: Very Easy
                      Problem Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/
*/


#include <stdio.h>

int main(){
	int N, Q, i, j;
	
	scanf("%d %d", &N, &Q);
	
	int arr[N];
	
	for(i = 0; i < N; i++){
	    scanf("%d", &arr[i]);
	}
	
	for(i = 0; i < Q; i++){
	    int inputType, X, L, R;
	    
	    scanf("%d", &inputType);
	    
	    if(inputType == 1){
	        scanf("%d", &X);
	        if(arr[X-1] == 0) arr[X-1] = 1;
	        else arr[X-1] = 0;
	    } else{
	        scanf("%d %d", &L, &R);
	        if(arr[R-1] == 1) printf("ODD\n");
	        else printf("EVEN\n");
	    }
	}
}

