
/*                    Name : Nazrul Islam Rakib
                      Judge: HackerEarth
                      problem: Toggle String 
                      Difficulty: very Easy
                      Problem Link: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/description/
*/


#include <stdio.h>
#include <string.h>

int main(){
	int i;
  	char str[200];
	scanf("%s", str);     
	
	for (i=0 ; i<strlen(str) ; i++){
	    
	    if( (int)str[i] >= 97){
	        
          str[i] = (int)str[i] - 32;

	    }else{
	        
       str[i] = (int)str[i] + 32;

	    }
	}

    
printf("%s",str);
	
}