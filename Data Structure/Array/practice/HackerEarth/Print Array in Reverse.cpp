/*                    Name : Aziz Ahmed
                      Judge: HackerEarth
                      problem: Print Array in Reverse
                      Difficulty: Very Easy
                      Problem Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/tutorial/
*/


#include <iostream>
 
using namespace std;
 
int main() {
    int N;
    cin >> N;
    
	int num[N];
	int i;
	for(i = 0; i < N; i++){
	    cin >> num[i];
	}
	
	for(i = N-1; i >= 0; i--){
	    cout << num[i] << endl;
	}
}