#include <iostream>
#include <vector>
#include <algorithm>
using namespace std; 
int main() {
	int n, m; 
	cin >> n >> m; 

    vector <int> v; 

	for (int i = 0; i < n; i++) {
		int a; 
        cin >> a; 
		v.push_back(a); 
	}

	sort(v.begin(), v.end()); 

	int s, e; 
	s = 0; 
	e = v.size() - 1;
	int result = 0; 
    
	while (s < e) {
		if (v[s] + v[e] < m) s++;
		else if (v[s] + v[e] > m)e--;
		else {
			result++; 
			e--; 
		}
	}
	cout << result; 
}