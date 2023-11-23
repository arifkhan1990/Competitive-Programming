#include <bits/stdc++.h>
using namespace std;

int solve(vector<int>& arr, int n, int k){
	
	int ans = 0, l = 0 , r = 0;

    unordered_map<long int, long int>m;
	while(r < n){
		if(m.find(arr[r]) == m.end())
			m[arr[r]] = 0;
		m[arr[r]]++;

		while(m.size() > k){
			m[arr[l]] = m[arr[l]] - 1;
			if(m[arr[l]] == 0){
				m.erase(arr[l]);
			}
			l++;
		}
		ans += r - l +1;
		r++;
	}
	return ans;
}
int goodSubarrays(vector<int>& arr, int n, int k)
{
	return (solve(arr, n , k) - solve(arr,n, k-1));
}
