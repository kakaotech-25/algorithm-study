#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> arr;

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;

	for(int i=0; i<n; i++) {
		int data;
		cin >> data;
		arr.push_back(data);
	}

	int start = 0, end = 1, cnt = 0;
	sort(arr.begin(), arr.end());

	while(start <= end && end < n) {
		if(arr[start] + arr[end] == m) {
			cnt++;
		}

		if(end == n-1) {
			start++;
			end = start + 1;
		} else {
			end++;
		}
	}
	cout << cnt;

	return 0;
}