/*                    Name : Arif Khan
                      Judge: Dimik Oj
                      University: Primeasia University
                      problem: প্রোগ্রামিং সমস্যা 24 - [৫২ সমস্যা বই] একান্তর উপাদান
                      Difficulty: Easy
                      Time Complexity: 0.3098 সেকেন্ড
                      Problem Link: https://dimikoj.com/problems/24/alternate-elements-by
*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t, a, b;
    scanf("%d",&t);
    for(int j = 0; j < t; j++) {

    	cin >> a;
        int ar[a+1];
        
    	for(int i = 0; i < a; i++) {
    		cin >> ar[i];
    	}
    	
    	for(int i = 0; i < a; i+=2) {
    		if( i != 0) cout << " ";
    		cout << ar[i];
    	}
    	cout << endl;
    }
    return 0;
}